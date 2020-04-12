/*                        JAVASCRIPT                         */
/*                                                           */
/*  Kyle Awah | Avita John | Riandra Maraj | Kyle Sukhdeo    */
/*  816012635 | 816012533  |   81601097    |   816014143     */
/*                                                           */
/*                                                           */
/*                       AFTR_MARKT                          */
/*                                                           */
/*                                                           */
/*                                                           */
/* Created on: 32/03/2020                                    */
/* INFO 2602 (Web Programming and Technologies 1)            */
/* Group Project - Storefront                                */


/* JQUERY FOR MOBILE MENU BAR */

$(document).ready(function(){
    $(".mobile_nav").on("click", function(){
        $("header nav ul").toggleClass("open");
        $("li.nav_bar_element").toggleClass("open");
        $(".final_icons").toggleClass("open");
				$(".box").toggleClass("open");
        $("#desktop_nav").remove();
    });
});

//refresh page on browser resize
$(window).bind('resize', function(e)
{
  this.location.reload(false); /* false to get page from cache */
});

$(document).ready(function(){
     if ($(window).width() > 900){

         $("#mobile_nav").remove();
         $("").remove();
         
         $("#desktop_nav").append(`
            <a href="/index">
                <img src="Icons/logo_clear.png" height="25" alt="HOME PAGE" onclick="/" />
            </a>
        `);
     } 
});