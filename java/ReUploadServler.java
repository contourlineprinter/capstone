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
		System.out.println("hello");
		//System.out.println(request.getParameter("xyslide"));
		//System.out.println(request.getParameter("skipslide"));
		String fname = request.getParameter("fname");
		int range = Integer.parseInt(request.getParameter("xyslide"));
		int skip = Integer.parseInt(request.getParameter("skipslide"));
		int min =  Integer.parseInt(request.getParameter("minslide"));
		String scale = request.getParameter("scale");
		
		fname = fname.replace("svg/", "");
		fname = fname.replace(".svg", "");
		
		System.out.println("scale " + scale);
		System.out.println("x y Range Slider " + range + " points to skip " + skip + " min area " + min);
		System.out.println("fname " + fname);
		
		
		// Command to write scale factor into the next folder
		Runtime.getRuntime().exec("python3 /var/lib/tomcat8/webapps/ROOT/WEB-INF/cgi/writescale.py " + scale);
		System.out.println("after");
		
		
		 String command = "python3 /var/lib/tomcat8/webapps/ROOT/conversion/imageConverter/convertFileInput-reg.py /var/lib/tomcat8/webapps/ROOT/images/" + fname +" /var/lib/tomcat8/webapps/ROOT/svg/";
		    Process p = null;
		    try {
		    	 p = Runtime.getRuntime().exec(command);
		    } catch (final IOException e) {
		    	request.setAttribute("message", "IOException: " + e);
		    	e.printStackTrace();
		    }
		   		  
		    //request.setAttribute("message", "fname " + fname);
		    
			// move to staging page with the response text
			getServletContext().getRequestDispatcher("/staging.jsp").include(request, response);
		
		

	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
		
		
	}

}
