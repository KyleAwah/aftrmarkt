/*                       JAVASCRIPT                          */
/*                                                           */
/*                       Kyle Awah                           */
/*                       816012635                           */
/*                                                           */
/*                                                           */
/*                       AFTR_MARKT                          */
/*                                                           */
/*                                                           */
/*                                                           */
/* Created on: 32/03/2020                                    */
/* INFO 2602 (Web Programming and Technologies 1)            */


var input = document.getElementById("input");
input.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        document.getElementById("MYBUTTON").click();
    }
});
