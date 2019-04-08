package app;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.commons.fileupload.FileItem;
import org.apache.commons.fileupload.disk.DiskFileItemFactory;
import org.apache.commons.fileupload.servlet.ServletFileUpload;

public class ImageUploadServler extends HttpServlet {
	// static final long serialVersionUID = 1L;
	private String file_directory;
	public String name;

	public ImageUploadServler() {
		super();
	}

	@Override
	public void init() throws ServletException {
		file_directory = getServletContext().getRealPath("/images");
	}

	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		response.getWriter().append("Served at: ").append(request.getContextPath());
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		System.out.println("looking in logs");
		if (ServletFileUpload.isMultipartContent(request)) {
			try {
				List<FileItem> multiparts = new ServletFileUpload(new DiskFileItemFactory()).parseRequest(request);

				for (FileItem item : multiparts) {
					if (!item.isFormField()) {
						name = new File(item.getName()).getName();
						item.write(new File(file_directory + File.separator + name));
					}
				}
				//Upload Worked
				request.setAttribute("message", "Image uploaded successfully");
				request.setAttribute("file", name);
				System.out.println("Image success message");
				System.out.println(name);

				
			} catch (Exception ex) {
				request.setAttribute("message", "Image upload failed due to: " + ex);
				ex.printStackTrace();
				// return to Index.jsp page with the response text
				getServletContext().getRequestDispatcher("/index.jsp").include(request, response);
				return; 
			}

		} else {
			request.setAttribute("message", "Unable to upload the file");
		}

		System.out.println("before try/catch");
		//Call python script on file

	    String command = "python3 /var/lib/tomcat8/webapps/ROOT/conversion/imageConverter/convertFileInput-reg.py /var/lib/tomcat8/webapps/ROOT/images/" + name +" /var/lib/tomcat8/webapps/ROOT/svg/";
	    Process p = null;
	    try {
	    	 p = Runtime.getRuntime().exec(command);
	    } catch (final IOException e) {
	    	request.setAttribute("message", "IOException: " + e);
	    	e.printStackTrace();
	    }

	    //Wait to get exit value
	    try {
	        final int exitValue = p.waitFor();
	        if (exitValue == 0)
	            System.out.println("Successfully executed the command: " + command);
	        else {
	            System.out.println("Failed to execute the following command: " + command + " due to the following error(s):");
	            try (final BufferedReader b = new BufferedReader(new InputStreamReader(p.getErrorStream()))) {
	                String line;
	                if ((line = b.readLine()) != null)
	                    System.out.println(line);
	            } catch (final IOException e) {
	                e.printStackTrace();
	                System.out.println("error1 " + e);
	            }                
	        }
	    } catch (InterruptedException e) {
	        e.printStackTrace();
	    }
	    
	    
		// move to staging page with the response text
		getServletContext().getRequestDispatcher("/staging.jsp").include(request, response);
	}

}
