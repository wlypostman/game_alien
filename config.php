<?php

/* User = postman <wlypostman@gmail.com>
 * 日期 ： 2013-07-3
 * 文件名： config
 */
$server = "127.0.0.1";
$use = "root";
$pws = "jintian";
$db = "text";

$link = mysql_connect($server, $use, $pws);
if($link == false){
  die("数据库连接错误，请检查连接参数！");
}
mysql_select_db($db);

?>