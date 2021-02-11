<?php

#günün bölümleri

$saat = date("A");

$geceyarisi= "00";
$sabah = "06";
$ogle  = "10";
$aksam = "17";
$gece  = "20";

if($saat > $geceYar && $saat < $sabah)
{
    echo "Selamlar!";
}

if($saat >= $sabah && $saat < $ogle)
{
    echo "Günaydın Efendim";
}

if($saat >= $ogle && $saat < $aksam)
{
    echo "Mutlu Bir Gün Dilerim";
}

if($saat >= $aksam && $saat < $gece)
{
    echo "İyi Akşamlar Dilerim";
}

if($saat >= $gece)
{
    echo "İyi Geceler";
}


?> 