#!/usr/bin/python3
import cgitb
cgitb.enable()
import cgi

def genMainPage():
    print("""
<!DOCTYPEhtml>
<html lang="en">
<!--

          ||||||||||||            Looking to improve The Monthly Bagel?
      ||||            ||||        If you know anything about writing,
    ||                    ||      research, or coding, we'd be happy
  ||                        ||    to have you help. Just get in contact
  ||                        ||    with us:
||                            ||
||            ||||            ||    Monthly Bagel : mothlybagel@gmail.com 
||          ||    ||          ||
||          ||    ||          ||  Feel free to play around with the code
||            ||||            ||  yourself if you don't want to work with us.
||                            ||  
  ||                        ||  
  ||                        ||    We hope you like our news website.
    ||                    ||      if you have any suggestions, comments,
      ||||            ||||        or concerns please let us know so we can
          ||||||||||||            make The Monthly Bagel even better!

 -The Monthly Bagel team
 
-->
<head>
        <meta charset="utf-8">
        <title>The Monthly Bagel</title>
        <style>
            /*title CSS*/
            #titlebar {
                min-width:500px;
                margin: 80px auto;
                position: relative;
                padding: 10px 5px;
                background: hsla(0,0%,100%,.3);
                font-size: 20px;
                font-family: 'Lora', serif;
                line-height: 1.5;
                border-radius: 10px;
                width: 60%;
                box-shadow: -5px 3px 30px black;
                overflow: hidden;
            }
            #titlebar::before {
                content: '';
                margin: -35px;
                position: absolute;
                top: 0;
                right: 0;
                bottom: 0;
                left: 0;
                filter: blur(10px);
                z-index: -1;
            }
            #titletext {
                font-size: 400%;
            }
            /*page 2 CSS*/
            #page2{
                color: white;border-width: 0px; border-radius: 5px; width:85%;
            }
            #about{
                padding: 10px 15px;
                margin: 10px 1%;
                background-color:white;
                color:black;
                border-width: 0px;
                border-radius: 5px;
                font-size:100%;
            }
            #navbar {
               
                background-color:rgba(255,255,255,0.2);
                overflow: hidden;
                margin: 0px 0px;
                padding: 5px 5px;
                width:100%;
                background: rgba(255,255,255, 0.1);
                font-family: 'Lora', serif;
                position: fixed;
                top:0px;
                left:0px;
                line-height: 1.5;
                border-radius:3px;
                color:white;
                z-index:5;

            }
            #navbar::before{
                content: '';
                margin: -35px;
                position: absolute;
                top: 0;
                right: 0;
                bottom: 0;
                left: 0;
                filter: blur(10px);
                z-index: -1;
            }
            /* Style the links inside the navigation bar */
            #navbar a {
                color: #f2f2f2;
                padding: 14px 16px;
                text-decoration: none;
                font-size: 20px;
            }
            /* Change the color of links on hover */
            #navbar a:hover {
                background-color:rgba(255,255,255,0.4);
            }
            /* Add a color to the active/current link */
            #navbar .active {
                background-color: #4CAF50;
                color: white;
            }
            #articleprev {
                min-width:500px;
                border-radius: 7px;
                border-width: 1px;
                width:85%;
                height:625px;
                
            }
            #oldarticles {
                min-width:500px;
                border-radius: 7px;
                border-width: 1px;
                width:85%;
                height:200px;
                
            }
            /*backgroung of home page*/
            body, .blurback::before, .lightblur::before{
                background: url(https://images5.alphacoders.com/754/thumb-1920-754580.jpg) 0 / cover fixed;
            }
            hr {
                margin: 5% 30%;
                border-color:rgb(255,255,255);
                border-width: 1px;
                border-style: solid;
            }
            .lightblur {
                margin: 20px 30%;
                position: relative;
                padding: 5px 5px;
                background: rgba(255,255,255, 0.1);
                font-family: 'Lora', serif;
                line-height: 1.5;
                border-radius: 10px;
                overflow: hidden;
                color:white;
            }
            .lightblur::before{
                content: '';
                margin: -35px;
                position: absolute;
                top: 0;
                right: 0;
                bottom: 0;
                left: 0;
                filter: blur(5px);
                z-index: -1;

            }

            /*formatting for the bagel logo in the titlebar*/
            .logo {
                width: 64px;
                height: 64px;
                padding-left:8px;
                padding-top: 8px;
                padding-right: 8px;
            }

        </style>
        <!--sets the favicon to the bagel logo-->
        <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
    </head>
    
    <body>
    <div id="home"></div>
        <center>
        <div class="lightblur" id="navbar">
            <a href="#home">Home</a>
            |
            <a href="#latestarticle">News</a>
            |
            <a href="#old">Older Articles</a>
            |
            <a href="#about">About</a>
        </div>
        <div id="titlebar" class="blurback">

            <!--use a table to keep everything aligned; otherwise the logo and text go to different lines-->
            <header>
            <table>
                <tbody><tr>
                    <td>
                    <!--bagel logo-->
                        <img class="logo" src="https://cdn4.iconfinder.com/data/icons/food-drinks-thick-version/33/bagel-512.png" alt="Bagel">
                    </td>
                    <td>
                        <div id="titletext"><center>The Monthly Bagel</center></div><!--pronounced BAH - GULL-->
                    </td>
                    <td>
                        <!--second Bagel logo-->
                        <img class="logo" src="https://cdn4.iconfinder.com/data/icons/food-drinks-thick-version/33/bagel-512.png" alt="Bagel">
                    </td>
                </tr>
            </tbody></table>
                </header>
             
        </div>
        <!--displays "welcome to the monthly Bagel", and "This month's article" -->
      
            <h1 class="lightblur">Welcome to<br>The Monthly Bagel</h1>
            <div id="latestarticle">
                 <h3 class="lightblur">This Month's Article</h3>
                <!--this displays a google doc inside the webpage-->
                <iframe id="articleprev" src="https://docs.google.com/document/d/e/2PACX-1vQ_zmtHEo4zuGlbxD44J5Bn25yissN7qn7rS2YI_vsHMI3H02zltPAa6ggtM-Fj0_WhtIrHl11NlXQt/pub?embedded=true"></iframe>
            </div>
            
            <h3 class="lightblur">Previous Articles</h3>
            <div id="old">
           <iframe id="oldarticles" src="https://docs.google.com/document/d/e/2PACX-1vR7om_elKCHJNek2CWdUk5rcUQ7tbUDLt9F1kJ0brrwUXHdj-67GrPUkRU2sk_d3US0jVJ2SvLfQqof/pub?embedded=true"></iframe>
           </div>
   
   <hr>

            <!--second page-->
            <div id="page2">
              
                <h3 class="lightblur">About</h3>
                </div></center> 
                    <div id="about">

                        The Monthly Bagel is a news site created by LAMS students
                        RR Strauss, LB Dare, and S Westcott, as well as a team
                        of volunteers helping us produce news mothly.<br><br>Want to help out?
                        Contact us at monthlybagel@gmail.com 
                        <a href=""><i>Join the Team!</i></a>
<!--end of website-->
                    </div>
                <footer>
                </footer>
</body>
</html>
""")
if __name__ == "__main__":
    #execute only if run as a script
    genMainPage()