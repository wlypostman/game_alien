
CREATE TABLE `bodys` (
 `id` int(9) unsigned NOT NULL AUTO_INCR
 `pid` int(9) unsigned NOT NULL,
 `bodys` text,
 `louceng` int(9) unsigned NOT NULL,
 `ip` varchar(15) NOT NULL,
 `times` datetime DEFAULT NULL,
 PRIMARY KEY (`id`)
)

 CREATE TABLE `nczt` (
 `id` int(9) unsigned NOT NULL AUTO_INCREM
 `title` varchar(200) DEFAULT NULL,
 `times` datetime DEFAULT NULL,
 PRIMARY KEY (`id`)
)