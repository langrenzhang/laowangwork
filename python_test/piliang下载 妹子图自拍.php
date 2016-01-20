<?php
define('DocumentRoot', dirname(__FILE__));
function curl_file_get_contents($durl, $timeout = 5, $refer = 'http://www.baidu.com') {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $durl);
    curl_setopt($ch, CURLOPT_TIMEOUT, $timeout);
    curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; QQBrowser/7.7.31732.400)');
    curl_setopt($ch, CURLOPT_REFERER, $refer);
    curl_setopt($ch, CURLOPT_COOKIE, "JYERN=0.775963805813623; jyean=1oVda1o0GzAC5tHXqcngD5XqLFNdMLIvhQh26WTfpaGLxNzqLHxnXfN1R3R0jhZ6W6JEtBAXfF0rM9It6h7NZcZmVNcaLYBjqDfgui0dALG3rIEus3VK5IeBE4yWBUgs0; WL=2; CNZZDATA2018550=cnzz_eid%3D1056381356-1417509991-%26ntime%3D1417509991");
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    $r = curl_exec($ch);
    curl_close($ch);
    return $r;
}
 
function JsJump($url, $time = 0) {
    $SleepTime = $time * 1000;
    echo '<script language="javascript">window.setTimeout("window.location=\'' . $url . '\'", ' . $time . ');</script>';
    exit();
}
 
function _mkdir($dir) {
    if (file_exists($dir)) {
        return true;
    }
 
    $u = umask(0);
    $r = @mkdir($dir, 0777);
    umask($u);
    return $r;
}
 
function getHtml($url){
    $page = curl_file_get_contents($url);
    return $page;
}
 
function downloadImg($imgUrl,$foldername = 'img'){
    $picpath = DocumentRoot.'/'.$foldername;
    _mkdir($picpath);
    $filename= basename($imgUrl);
    $img = file_get_contents($imgUrl);
    if ($img) {
        file_put_contents($picpath.'/'.$filename, $img);
        return true;
    }
    return false;
}
 
function findPage($html){
    preg_match('/<a class=\"next page-numbers\" href=\"http:\/\/www.mzitu.com\/share\/comment-page-(.*?)#comments\"><\/a>/is', $html,$matches);
    return $matches;
}
 
function findList($html){
    preg_match_all('/<p><img src=\"(.*?)\" alt=\"(.*?)\" \/><\/p>/is', $html,$matches);
    return $matches;
}
 
$p = isset($_GET['p'])?max(1,$_GET['p']):1;
$home = getHtml('http://www.mzitu.com/share/comment-page-'.$p);
$list = findList($home);
echo "now downloading page ".$p."...";
if (is_array($list[1])) {
    foreach ($list[1] as $key => $value) {
        downloadImg($value);
    }
}
 
$page = findPage($home);
if ($page[1] AND $page[1]>$p) {
    JsJump('/mzi.php?p='.$page[1]);
}else{
    exit("finished");
}