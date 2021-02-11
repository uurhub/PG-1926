<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP-ASAL SAYI</title>
</head>
<body>
<div>
    <h1>Asal Sayı Bulma</h1>

        
        <form>
            <label>Sayıyı giriniz:</label>
            <input type="number" id="fname" name="sayi" value="Bir Sayıyı Giriniz:"><br><br>
            <input type="submit" value="Bu sayı asal sayı mı?">
        </form><br>
            <?php 
                
                $degisken = $_GET["sayı"];

                $asal=0; $i=2;
 
                do
                {
                    if ($degisken % $i == 0)
                    {
                        $asal = 1;
                    }
                    $i++;
                }
                while($i<$degisken);
                 
                if ($asal != 1)
                {
                    $sonuc="Belirtilen Sayı asaldır";
                }
                else if ($degisken == 2)
                {
                    $sonuc="Belirtilen Sayı Asaldır";
                }
                else 
                {
                    $sonuc="Belirtilen Sayı Asal Değildir"; 
                }

                echo $degisken;
                echo $sonuc;
                ?>
                
                
                    
            
     </div>
</body>
</html>