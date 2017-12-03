
CREATE TABLE IF NOT EXISTS `environments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(1024) NOT NULL,
  `create_time` timestamp NOT NULL default CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `variable1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `env_id` int(11) NOT NULL,
  `key` varchar(1024) NOT NULL,
  `value` varchar(1024) NOT NULL,
  `create_time` timestamp NOT NULL default CURRENT_TIMESTAMP,
  FOREIGN KEY (env_id) REFERENCES environments(id),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;



