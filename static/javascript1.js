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


var input = document.getElementById("input");
input.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        document.getElementById("MYBUTTON").click();
    }
});