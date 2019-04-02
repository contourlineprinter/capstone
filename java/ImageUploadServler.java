package app;

import java.io.File;
import java.io.IOException;
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
						String name = new File(item.getName()).getName();
						item.write(new File(file_directory + File.separator + name));
					}
				}
				//Upload Worked
				request.setAttribute("message", "Image uploaded successfully");
				
				//Call python script on file
				Process p = Runtime.getRuntime().exec("python3 /conversion/imageConverter/convertFileInput.py");
				
			} catch (Exception ex) {
				request.setAttribute("message", "Image upload failed due to: " + ex);
				ex.printStackTrace();
			}

		} else {
			request.setAttribute("message", "Unable to upload the file");
		}

		// return to Index.jsp page with the response text
		getServletContext().getRequestDispatcher("/index.jsp").include(request, response);
	}

}
