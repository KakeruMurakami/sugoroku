$(function(){
        var masu=0;
        var nokori;
        var rand;
        $("#saikoro").on("click", function(){
             rand=Math.floor(Math.random()*6)+1;
            //console.log(rand);
            masu+=rand;
            nokori=30-masu;
            var myobj=document.getElementById("sugo");
            myobj.textContent="サイコロの目は"+rand+"。現在"+masu+"マス進みました。残りマスは"+nokori+"マスです。";
            
            
            if(nokori<=0){
                myobj.textContent="GOAL!!";
            }
            
        });
        
        
        
        
        
        
       
 })