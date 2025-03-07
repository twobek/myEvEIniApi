create table if not exists param
      (param_type varchar(100) primary key
      ,param_text text
      ,param_number integer
      ,param_date date
      )
;

insert into param
      (param_type)
values('LAST_TYPE_IMPORT')
;