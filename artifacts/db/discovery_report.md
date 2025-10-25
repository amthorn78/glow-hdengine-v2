 ?column? |                                                      version                                                       
----------+--------------------------------------------------------------------------------------------------------------------
 version  | PostgreSQL 17.6 (Debian 17.6-2.pgdg13+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
(1 row)

   ?column?   | current_user 
--------------+--------------
 current_user | postgres
(1 row)

  ?column?   | current_setting 
-------------+-----------------
 search_path | "$user", public
(1 row)

 ?column? | string_agg 
----------+------------
 schemas  | public
(1 row)

   ?column?   |         string_agg          
--------------+-----------------------------
 roles_sample | hde_owner, hde_rw, postgres
(1 row)

