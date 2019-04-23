
// function fetchdata(context){
//     $.ajax({
//         url: '/homepage/index/',
//         success: function(response){
//         console.log("refreshed");
                     
//             $((function(context) {

//                 if(context.my_titles.length > 0)
//                 {
//                     // var y;
//                     // var old_items = [];
//                     // for(y = 0; y < context.old_titles.length; y++)
//                     // {
//                     //     old_items[y] = context.old_titles[y] + context.old_prices[y] + context.old_years[y] + context.old_cities[y] + context.old_sizes[y];
//                     // }

//                     var i;
//                     var items = "";
//                     for(i = 0; i < context.my_titles.length; i++)
//                     {
//                         // if(jQuery.inArray(context.my_titles[i] + context.my_prices[i] + context.my_years[i] + context.my_cities[i] + context.my_sizes[i], old_items) == -1) //if not in the array
//                         // {

//                             items += context.my_titles[i] + " " + context.my_prices[i] + ",  "; 
//                         // }                  
//                     }
//                     if (items.length > 0)
//                     {
//                         return function() {
//                             alert(items);     
//                         }
//                     }    
                    
//                 }
            
//             })(DMP_CONTEXT.get()));
//         }
//     });   
// }

// $(document).ready(function(){
// setInterval(fetchdata,600000); //every 10 minutes = 600000
// });

jQuery(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });
});

// $((function(context) {

//     if(context.my_titles.length > 0)
//     {
//         var i;
//         var items = "";
//         for(i = 0; i < context.my_titles.length; i++)
//         {
//            items += context.my_titles[i] + context.my_prices[i] + ",  ";   
//         }
//         return function() {
//             alert(items);     
//         }
//     }
   
// })(DMP_CONTEXT.get()));
