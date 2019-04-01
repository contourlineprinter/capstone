package app;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class ImageGallery extends HttpServlet {
	private static final long serialVersionUID = 1L;	
	private String file_directory;

    public ImageGallery() {
        super();
    }
    
    @Override
    public void init() throws ServletException {
    	file_directory = getServletContext().getRealPath("/images");
    }
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {		
		List<String> images = new ArrayList<>();
        try {        	
           File f = new File(file_directory);           
           if(f.exists() && f.isDirectory()) {
        	  String[] files = f.list();
        	  for(String str: files) {
        		  File f1 = new File(file_directory + File.separator + str);
        		  if(f1.isFile()) {
        			  images.add("images" + File.separator + str);
        		  }
        	  }
           }            
           request.setAttribute("message", "Fethed images successfully");
        } catch (Exception ex) {
           request.setAttribute("message", "Images not found: " + ex);
           ex.printStackTrace();
        }          
      
        request.setAttribute("images", images);
        getServletContext().getRequestDispatcher("/gallery.jsp").include(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
