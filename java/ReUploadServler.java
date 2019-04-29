package app;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class ReUploadServler extends HttpServlet {
	private static final long serialVersionUID = 1L;	
	//private String file_directory;
	

    public ReUploadServler() {
        super();
    }
    
    @Override
    public void init() throws ServletException {
    	//file_directory = getServletContext().getRealPath("/images");
    
    }
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {		

	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//doGet(request, response);
		System.out.println("--- Reupload ---");
		
		// Get form parameters

		String fname = request.getParameter("fname");
		int range = Integer.parseInt(request.getParameter("xyslide"));
		int skip = Integer.parseInt(request.getParameter("skipslide"));
		int min =  Integer.parseInt(request.getParameter("minslide"));
		String scale = request.getParameter("scale");
		

		// Parse filename
		fname = fname.replace("svg/", "");
		fname = fname.replace(".svg", "");
		fname = fname.substring(0, fname.indexOf("?"));
		
		// Testing 
		System.out.println("-- scale " + scale);
		System.out.println("-- x y Range Slider " + range + " points to skip " + skip + " min area " + min);
		System.out.println("-- fname " + fname);
		
		// Returns the file to load on response 

		fname = fname.replace("svg/", "");
		fname = fname.replace(".svg", "");
		
		System.out.println("-- scale " + scale);
		System.out.println("-- x y Range Slider " + range + " points to skip " + skip + " min area " + min);
		System.out.println("-- fname " + fname);

		request.setAttribute("file", fname); // give a file attribute to return as the response
		
		
		// Command to write scale factor into the next folder
		Runtime.getRuntime().exec("python3 /var/lib/tomcat8/webapps/ROOT/WEB-INF/cgi/writescale.py " + scale);
		System.out.println("-- wrote scale value");

		request.setAttribute("message", "wrote scale " + scale);
		
		
		String command = "";  // init command variable
		
		// Get radio button input
		String conversionType = request.getParameter("conversionType");
		System.out.println("-- conversionType: " + conversionType);
			
		// See what radial button is selected
		if (conversionType == null){
			System.out.println("-- default selected");
			command = "python3 /var/lib/tomcat8/webapps/ROOT/conversion/imageConverter/convertFileInput-reg.py /var/lib/tomcat8/webapps/ROOT/images/" + fname +" /var/lib/tomcat8/webapps/ROOT/svg/ " + range + " " + skip + " " + min;
		//	command = "";
		} else if (conversionType.equals("highquality")){  // use highquality
			System.out.println("-- high quality selected");
			command = "python3 /var/lib/tomcat8/webapps/ROOT/conversion/imageConverter/convertFileInput-highQuality.py /var/lib/tomcat8/webapps/ROOT/images/" + fname + " /var/lib/tomcat8/webapps/ROOT/svg/ " + range + " " + skip + " " + min;
		} else if (conversionType.equals("hq2")){  // use canny
			System.out.println("-- hq 2");
			command = "python3 /var/lib/tomcat8/webapps/ROOT/conversion/imageConverter/convertFileInput_HQ.py /var/lib/tomcat8/webapps/ROOT/images/" + fname + " /var/lib/tomcat8/webapps/ROOT/svg/ " + range + " " + skip + " " + min;
		} else { //default
			
		}
		

		 
	    Process p = null;
	    
	    // Try to exec the python command
	    try {
	    	 p = Runtime.getRuntime().exec(command);
	    } catch (final IOException e) {
	    	request.setAttribute("message", "IOException: " + e);
	    	e.printStackTrace();
	    }
	    
	    //Wait to get exit value
	    try {
	        final int exitValue = p.waitFor();
	        if (exitValue == 0) {  // hits this if python runs with no errors
	            System.out.println("-- Successfully executed the command: " + command);
	        	request.setAttribute("message", "Reupload Successful.  When ready place car in the top left of your paper and hit print");
	        }
	        
	        else {  // hits this code block if the python code has an error
	            System.out.println("-- Failed to complete/execute the following command: " + command);
				request.setAttribute("message", "May have failed to regenerate svg for file " + fname);
				// return to Index.jsp page with the response text
				//getServletContext().getRequestDispatcher("/staging.jsp").include(request, response);
				//return; 
	                            
	        }
	    } catch (InterruptedException e) {
	        e.printStackTrace();
	    }
	   		  
	    
	    
		// move to staging page with the response text
		getServletContext().getRequestDispatcher("/staging.jsp").include(request, response);
	
	

		
		
	}

}
