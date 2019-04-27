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

import java.util.regex.*;

public class ImageUploadServler extends HttpServlet {
	// static final long serialVersionUID = 1L;
	private String file_directory;
	public String name;
	private static Pattern fileExtnPtrn = Pattern.compile("([^\\s]+(\\.(?i)(jpg|png|bmp|jpeg))$)");

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
		
		if (ServletFileUpload.isMultipartContent(request)) {
			try {
				List<FileItem> multiparts = new ServletFileUpload(new DiskFileItemFactory()).parseRequest(request);

				for (FileItem item : multiparts) {
					if (!item.isFormField()) {
						name =  new File(item.getName()).toString();
						// remove spaces, make lowercase
						name = name.replaceAll(" ", "_"); 
						
						// check for valid file extension
						Matcher mtch = fileExtnPtrn.matcher(name);
				        if(!mtch.matches()){

							request.setAttribute("message", "Unsupported file format,  please use a common image format such as .jpg or .png ");
							getServletContext().getRequestDispatcher("/index.jsp").include(request, response);
							return; 	
						}
						
						System.out.println(item.getName());
						System.out.println("filename: " + name);
						item.write(new File(file_directory + File.separator + name));
					}
				}
				//Upload Worked
				request.setAttribute("message", "Image uploaded");
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
	            System.out.println("Failed to complete/execute the following command: " + command);
				request.setAttribute("message", "May have failed to generate svg for file " + name);
				// return to Index.jsp page with the response text
				//getServletContext().getRequestDispatcher("/index.jsp").include(request, response);
				//return; 
	                            
	        }
	    } catch (InterruptedException e) {
	        e.printStackTrace();
	    }
	    
	    
		// move to staging page with the response text
		getServletContext().getRequestDispatcher("/staging.jsp").include(request, response);
	}

}
