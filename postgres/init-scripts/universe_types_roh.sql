begin
set local search_path = 'public'
CREATE TABLE if not exists universe_types_roh (type_id INTEGER PRIMARY KEY
                                              ,creation_ts date
                                              ,api_page integer
);
commit;