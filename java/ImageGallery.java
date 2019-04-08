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
	private String file_directory2;

    public ImageGallery() {
        super();
    }
    
    @Override
    public void init() throws ServletException {
    	file_directory = getServletContext().getRealPath("/images");
    	file_directory2 = getServletContext().getRealPath("/svg");
    }
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {		
		
		// Get images from images folder
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
        
		// Get svgs from svg folder
		List<String> svg = new ArrayList<>();
        try {        	
           File f2 = new File(file_directory2);           
           if(f2.exists() && f2.isDirectory()) {
        	  String[] files2 = f2.list();
        	  System.out.println("cp1");
        	  for(String str2: files2) {
        		  File f3 = new File(file_directory2 + File.separator + str2);
        		  if(f3.isFile()) {
        			  svg.add("svg" + File.separator + str2);
        		  }
        	  }
        	  System.out.println("cp2");
           }
           else {
        	   System.out.println("directory does not exist");
           }
           System.out.println("Fethed svg successfully");
        } catch (Exception ex) {
           request.setAttribute("message", "Images not found: " + ex);
           ex.printStackTrace();
        }  
        System.out.println("size of svg" + svg.size());
        System.out.println("size of images" + images.size());
        request.setAttribute("svg", svg);
        request.setAttribute("images", images);
        getServletContext().getRequestDispatcher("/gallery.jsp").include(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
