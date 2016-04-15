DROP TABLE if exists subscribers;
CREATE TABLE subscribers (
	id char(10) NOT NULL,
	id_project int NOT NULL,
	email varchar(128) NOT NULL,
	PRIMARY KEY (id),
	INDEX (email)
	) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into sequencers (id, s_partition, active_stage, size, check_sum_size, name ,type, s_table, ordered)
values('b','00','000',4,0,'subscribers','STR','s_subscribers',false);

DROP TABLE if exists s_subscribers;
CREATE TABLE s_subscribers (
	id char(10) NOT NULL,
	active_stage char(3)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;