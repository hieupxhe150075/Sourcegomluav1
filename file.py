<?php
system('clear');
//colors
$red="\033[1;31m";
$green="\033[1;32m";
$yellow="\033[1;33m";
$blud="\033[1;34m";
$res="\033[1;35m";
$nau="\033[1;36m";
$trang="\033[1;37m";



if(file_exists("cfg.php") != true){
      
echo $green."Nhập Token App Gom Lúa:";
$token = trim(fgets(STDIN));
echo $green."Nhập Coockie Facebook:";
$token = trim(fgets(STDIN));
$cookie = trim(fgets(STDIN));
$k = fopen("cfg.php","a+");
fwrite($k, "<?php
$");
fwrite($k, "token = '$token';
$");
fwrite($k, "cookie = '$cookie';
?>");
fclose($k);
}
include("cfg.php");

while(true){
for($i=$time=20;$i>-1;$i--){
}

//lấy job
 
$urljob = "http://gomlua.com:1337/cpi/listCampaignFacebook?os=android&type=like_post_fanpage";

$curljob = curl_init();
curl_setopt_array($curljob, array(
//  CURLOPT_PORT => "1337",
  CURLOPT_URL => "$urljob",
  CURLOPT_ENCODING => "",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_SSL_VERIFYPEER => false,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => array(
'If-None-Match: W/"e8e-XfCVF7JyRjnhGExuviLm+jNHot8"',
"app_token: $token",
"User-Agent: Dalvik/2.1.0 (Linux; U; Android 5.0.2; SM-A300H Build/LRX22G)",
"Connection: Keep-Alive",
"Accept-Encoding: gzip"
)));
$curljob1 = curl_exec($curljob); curl_close($curljob);
$json = json_decode($curljob1,true);
$uid = $json["data"]["list"]["0"]["campaign_id"];
$type = $json["data"]["list"]["0"]["react_type"]; 
$link_id = $json["data"]["list"]["0"]["link_id"];
$amount = $json["data"]["list"]["0"]["amount"];
echo $nau."|Nhiệm Vụ| $reg$type$green\n";sleep(15);
echo $nau."|link id | $reg$link_id\n";sleep(14);
sleep(5);
//checkjob

$urlcheckjob = "http://gomlua.com:1337/cpi/checkLinkLike?link_id=".$link_id; 

$curlcheckjob = curl_init();
curl_setopt_array($curlcheckjob, array(
//  CURLOPT_PORT => "1337",
  CURLOPT_URL => "$urlcheckjob",
  CURLOPT_ENCODING => "",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_SSL_VERIFYPEER => false,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => array(
"app_token: $token",
"User-Agent: Dalvik/2.1.0 (Linux; U; Android 5.0.2; SM-A300H Build/LRX22G)",
"Connection: Keep-Alive",
"Accept-Encoding: gzip"
)));
$curlcheckjob1 = curl_exec($curlcheckjob); curl_close($curlcheckjob);
$json1 = json_decode($curlcheckjob1,true);
$like_count = $json1["data"]["like_count"];
echo "$nau|Tổng ".$type."Còn Lại ".$reg.$like_count."|\n";sleep(15);
//like
if($type == "LIKE"){

$url = "https://mbasic.facebook.com/".$uid;
$head = array (
"Host: mbasic.facebook.com",
"upgrade-insecure-requests: 1",
"save-data: on",
"user-agent: Mozilla/5.0 (Linux; Android 5.1.1; SM-J320G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
"accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*"."/"."*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"sec-fetch-site: same-origin",
"sec-fetch-mode: navigate",
"sec-fetch-user: ?1",
"sec-fetch-dest: document",
"accept-language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
"cookie: $cookie",
);
$ch = curl_init();
curl_setopt_array ($ch, array (
CURLOPT_URL => $url,
CURLOPT_FOLLOWLOCATION => false,
CURLOPT_RETURNTRANSFER => 1,
CURLOPT_POST => 1,
CURLOPT_HTTPGET => true,
CURLOPT_SSL_VERIFYPEER => 0,
CURLOPT_HTTPHEADER => $head,
CURLOPT_HEADER => true,
CURLOPT_ENCODING => TRUE));
$data = curl_exec($ch);
if (strpos($data,"xs=deleted") == true){

} else {
$one = explode("location: ",$data);
$two = explode("rdr",$one[1]);

$url = $two[0]."rdr";
curl_setopt_array ($ch, array (
CURLOPT_URL => $url,
CURLOPT_FOLLOWLOCATION => false,
CURLOPT_RETURNTRANSFER => 1,
CURLOPT_POST => 1,
CURLOPT_HTTPGET => true,
CURLOPT_SSL_VERIFYPEER => 0,
CURLOPT_HTTPHEADER => $head,
CURLOPT_HEADER => true,
CURLOPT_ENCODING => TRUE));
$data = curl_exec($ch);
$one = explode("/a/like.php?",$data);
$two = explode('"',$one[1]);

$url = "https://mbasic.facebook.com/a/like.php?".htmlspecialchars_decode($two[0]);
curl_setopt_array ($ch, array (
CURLOPT_URL => $url,
CURLOPT_FOLLOWLOCATION => false,
CURLOPT_RETURN,
TRANSFER => 1,
CURLOPT_POST => 1,
CURLOPT_HTTPGET => true,
CURLOPT_SSL_VERIFYPEER => 0,
CURLOPT_HTTPHEADER => $head,
CURLOPT_HEADER => true,
CURLOPT_ENCODING => TRUE,));
$data = curl_exec($ch);
}
}
//phần love

if($type == "LOVE" or $type == "WOW" ){
if($type == "LOVE"){
$cx = 2;
}
if($type == "WOW"){
$cx = 5;
}
$head = array(
"Host: mbasic.facebook.com",
"upgrade-insecure-requests: 1",
"save-data: on",
"user-agent: Mozilla/5.0 (Linux; Android 5.1.1; SM-J320G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
"accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*"."/"."*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"sec-fetch-site: same-origin",
"sec-fetch-mode: navigate",
"sec-fetch-user: ?1",
"sec-fetch-dest: document",
"accept-language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
"cookie: $cookie",
);
$url = "https://mbasic.facebook.com/".$uid;

$mr = curl_init();
curl_setopt_array($mr, array(
CURLOPT_URL => $url,
CURLOPT_FOLLOWLOCATION => false,
CURLOPT_RETURNTRANSFER => 1,
CURLOPT_POST => 1,
CURLOPT_HTTPGET => true,
CURLOPT_SSL_VERIFYPEER => 0,
CURLOPT_HEADER => true,
CURLOPT_ENCODING => TRUE,
CURLOPT_HTTPHEADER => $head));
$mr2 = curl_exec($mr); curl_close($mr);
$link2 = explode("location: ", $mr2);
$link1 =  explode("rdr", $link2[1]);
$link = htmlspecialchars_decode($link1[0]);

$url = $link."rdr";
$mr = curl_init();
curl_setopt_array($mr, array(
CURLOPT_URL => $url,
CURLOPT_FOLLOWLOCATION => false,
CURLOPT_RETURNTRANSFER => 1,
CURLOPT_POST => 1,
CURLOPT_HTTPGET => true,
CURLOPT_SSL_VERIFYPEER => 0,
CURLOPT_HEADER => true,
CURLOPT_ENCODING => TRUE,
CURLOPT_HTTPHEADER => $head));
$mr2 = curl_exec($mr); curl_close($mr);
$a2 = explode("/reactions/picker/", $mr2);
$a1 = explode('"', $a2[1]);
$a = htmlspecialchars_decode($a1[0]);
$url = "https://mbasic.facebook.com/reactions/picker/".$a;

$mr = curl_init();
curl_setopt_array($mr, array(
CURLOPT_URL => $url,
CURLOPT_FOLLOWLOCATION => false,
CURLOPT_RETURNTRANSFER => 1,
CURLOPT_POST => 1,
CURLOPT_HTTPGET => true,
CURLOPT_SSL_VERIFYPEER => 0,
CURLOPT_HEADER => true,
CURLOPT_ENCODING => TRUE,
CURLOPT_HTTPHEADER => $head));
$mr2 = curl_exec($mr); curl_close($mr);
$love2 = explode("/ufi/reaction/", $mr2);
$love1 = explode('"', $love2[$cx]);
$love = htmlspecialchars_decode($love1[0]);
$url = "https://mbasic.facebook.com/ufi/reaction/".$love;
$mr = curl_init();
curl_setopt_array($mr, array(
CURLOPT_URL => $url,
CURLOPT_FOLLOWLOCATION => false,
CURLOPT_RETURNTRANSFER => 1,
CURLOPT_POST => 1,
CURLOPT_HTTPGET => true,
CURLOPT_SSL_VERIFYPEER => 0,
CURLOPT_HEADER => true,
CURLOPT_ENCODING => TRUE,
CURLOPT_HTTPHEADER => $head));
$mr2 = curl_exec($mr); curl_close($mr);
}
sleep(2);
$urlsuccess = "http://gomlua.com:1337/cpi/likeSuccess?link_id=".$link_id."&like_old=".$like_count;

$curlsuccess = curl_init();
curl_setopt_array($curlsuccess, array(
//  CURLOPT_PORT => "1337",
  CURLOPT_URL => "$urlsuccess",
  CURLOPT_ENCODING => "",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_SSL_VERIFYPEER => false,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => array(
"app_token: $token",
"User-Agent: Dalvik/2.1.0 (Linux; U; Android 5.0.2; SM-A300H Build/LRX22G)",
"Connection: Keep-Alive",
"Accept-Encoding: gzip"
)));
$curlsuccess1 = curl_exec($curlsuccess); curl_close($curlsuccess);
$json2 = json_decode($curlsuccess1,true);
$message = $json2["message"];
if($message == 'Quá Thời Gian Làm Job, Đã Báo Kênh Tool Làm Lại !'){
echo $red."[".$message."]"."\n"; sleep(15);
}else{
echo $nau."|nhận được ".$amount."|"."\n";sleep(30);
for($time=$r;$time>-1;$time--){
echo $res."Đang Load Job $time giây "."\r";
}
}
echo "------------------------"."---------------------------------------"."\n";
}
