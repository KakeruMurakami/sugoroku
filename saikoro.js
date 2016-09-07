
function onButtonClick(){

        //定義
        var p1masu=0;
        var p2masu=0;
        var p1nokori=1;
        var p2nokori=1;
        var rand;
        var val2Text = $('#my-number2').val();
        var val2 = Number(val2Text); //マス数の取得
        var val1Text = $('#my-number1').val();
        var val1 = Number(val1Text); //プレイヤー数の取得
        
     

        document.getElementById("p2saikoro").disabled = "true";

        //player1のターン
        $("#p1saikoro").on("click", function(){
             rand=Math.floor(Math.random()*12)+1;
            //console.log(rand);
            if(p1nokori>0){
                p1masu+=rand;
                p1nokori=val2-p1masu;
                var myobj=document.getElementById("p1sugo");
                myobj.textContent="サイコロの目は"+rand+"。現在"+p1masu+"マス目です。残りマスは"+p1nokori+"マスです。";
                if(p1nokori==0){
                    myobj.textContent="GOAL!!";
                }
            }


            else if(p1nokori<0){
                p1masu-=rand;
                p1nokori=val2-p1masu;
                var myobj=document.getElementById("p1sugo");
                myobj.textContent="サイコロの目は"+rand+"。現在"+p1masu+"マス目です。残りマスは"+p1nokori+"マスです。";
                if(p1nokori==0){
                    myobj.textContent="GOAL!!";
                }
            }
            if(p2nokori!=0){
            document.getElementById("p1saikoro").disabled = "true";
            document.getElementById("p2saikoro").disabled = "";
            }

        });

        //player2のターン
        $("#p2saikoro").on("click", function(){
             rand=Math.floor(Math.random()*12)+1;
            //console.log(rand);
            if(p2nokori>0){
                p2masu+=rand;
                p2nokori=val2-p2masu;
                var myobj=document.getElementById("p2sugo");
                myobj.textContent="サイコロの目は"+rand+"。現在"+p2masu+"マス目です。残りマスは"+p2nokori+"マスです。";
                if(p2nokori==0){
                    myobj.textContent="GOAL!!";
                }
            }


            else if(p2nokori<0){
                p2masu-=rand;
                p2nokori=val2-p2masu;
                var myobj=document.getElementById("p2sugo");
                myobj.textContent="サイコロの目は"+rand+"。現在"+p2masu+"マス目です。残りマスは"+p2nokori+"マスです。";
                if(p2nokori==0){
                    myobj.textContent="GOAL!!";
                }
            }
            if(p1nokori!=0){
            document.getElementById("p1saikoro").disabled = "";
            document.getElementById("p2saikoro").disabled = "true";
            }
        });
    
}

function reload(){
    location.reload();
}


    

    
        
        
        
        