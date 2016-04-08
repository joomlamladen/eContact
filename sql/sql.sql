insert into sequencers (id, s_partition, active_stage, size, check_sum_size, name ,type, s_table, ordered)
values('b','00','000',4,0,'subscribers','STR','s_subscribers',false);

CREATE TABLE subscribers (
	id char(10) PRIMARY KEY,
	email varchar(128) NOT NULL UNIQUE
	);