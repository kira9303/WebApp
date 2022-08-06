# WebApp

Created a webapp using python, flask, html & css


For the web app to work follow:-
1)Create a database in MysQL named 'database'
2) database password = "password"
3) Create Tables :- append, tasks, team, user tables with the respective with the following shcemas:-

===== for append table =====
CREATE TABLE `append` (
  `id_team` bigint(20) NOT NULL,
  `status` varchar(45) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `id_task` bigint(20) NOT NULL,
  PRIMARY KEY (`id_team`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4

==== for tasks table ======
CREATE TABLE `tasks` (
  `id` bigint(20) NOT NULL,
  `task_name` varchar(45) DEFAULT NULL,
  `task` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4_general_ci;


====== for team table ======

CREATE TABLE `team` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Team_name` varchar(45) DEFAULT NULL,
  `Leader_name` varchar(45) DEFAULT NULL,
  `Name_1` varchar(45) DEFAULT NULL,
  `Name_2` varchar(45) DEFAULT NULL,
  `Name_3` varchar(45) DEFAULT NULL,
  `Name_4` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8mb4_general_ci;


==== for user table =====

CREATE TABLE `user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4_general_ci;


4) Run the app.py and open the localhost (127.0.0.1:5000) on the browser to access the web app




