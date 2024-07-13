use players;

create table employee(ssn Integer Primary Key, Name Varchar(20), dept Varchar(20));
insert into employee values(1,"Raj","Testing");
insert into employee values(2,"Ram","Analysis");
insert into employee values(3,"Rakesh","Planning");
insert into employee values(4,"Charan","Testing");
insert into employee values(5,"Ayush","Analysis");

create table project(p_no Varchar(8) primary key,p_name varchar(20), p_domain varchar(15));
insert into project values("S01","library db","database");
insert into project values("S02","Student db","cloud");
insert into project values("S03","hostel db","Security");
select * from project;

create table works_on(SSN integer, p_no varchar(8), no_hours integer, foreign key(SSN) references employee(SSN), foreign key(p_no) references project(p_no));
insert into works_on values(1,"S01",57);
insert into works_on values(2,"S02",42);
insert into works_on values(3,"S01",32);
insert into works_on values(4,"S03",30);
insert into works_on values(5,"S03",45);

#1
select employee.* from employee
join works_on on employee.ssn = works_on.ssn
join project on project.p_no = works_on.p_no
where project.p_domain='database';
#1
select ssn,name,dept from employee
where ssn in(select ssn from works_on where p_no in(select p_no from project where p_domain='database'));
#2
select count(ssn) as Num_Employees,dept from employee 
group by dept;
#3
update works_on set p_no='S02'  where ssn=5;

##############################

create table supplier(sid int primary key, sname varchar(20), saddr varchar(30));
insert into supplier values(103,"Ram","Ramnagar");
insert into supplier values(104,"Raj","Rajnagar");
insert into supplier values(105,"Ayush","Rajnagar");

create table part(pid integer primary key, pname varchar(20), pcolor varchar(20));
insert into part values(1,"mouse","black");
insert into part values(2,"keyboard","white");
insert into part values(3,"monitor","grey");

create table supply( sid integer, pid integer, no_of_parts integer, foreign key(sid) references supplier(sid), foreign key(pid) references part(pid));
insert into supply values(103,3,300);
insert into supply values(105,2,450);
insert into supply values(103,1,700);
insert into supply values(104,2,350);
insert into supply values(105,3,200);

#1
select part.* from part
join supply on supply.pid = part.pid
join supplier on supply.sid = supplier.sid
where supplier.sname = "ram";
#1
select pid, pname, pcolor from part
where pid in(select pid from supply where sid in(select sid from supplier where sname = 'ram'));

#2
select supplier.sname from supplier
join supply on supply.sid = supplier.sid
join part on supply.pid = part.pid
where pname = "keyboard";

#3
delete from supply
where pid in(Select pid from part where  pcolor="black");
SET SQL_SAFE_UPDATES = 0;
delete from part where pcolor='white';

########################

create table boat(bid integer primary key, bname varchar(20), bcolor varchar(20));
insert into boat values(101,'blue','blue bird');
insert into boat values(102,'red','red bird');
insert into boat values(103,'green','green bird');
insert into boat values(104,'black','black bird');

create table sailor(sailor_id integer primary key, sname varchar(20), sage varchar(20));
insert into sailor values(201,'Ram',23);
insert into sailor values(202,'Raj',24);
insert into sailor values(203,'Radha',31);

create table reservation(bid integer, sailor_id integer, day_of_week varchar(10), foreign key(bid) references boat(bid), foreign key(sailor_id) references sailor(sailor_id));
insert into reservation values(101,201,'Monday');
insert into reservation values(102,202,'Tuesday');
insert into reservation values(101,202,'Wednesday');
insert into reservation values(101,203,'Thursday');
insert into reservation values(103,203,'Friday');
insert into reservation values(103,202,'Monday');
insert into reservation values(102,201,'Wednesday');

#1
select boat.* from boat
join reservation on reservation.bid = boat.bid
join sailor on sailor.sailor_id = reservation.sailor_id
where sailor.sname = "ram";

#2
select reservation.bid from reservation
group by reservation.bid
having count(distinct sailor_id) = (select count(*) from sailor);

#3
select sailor.sname, count(reservation.bid) as no_of_boats from sailor
join reservation on sailor.sailor_id = reservation.sailor_id
group by sailor.sailor_id;

create table customer(cid integer primary key, cname varchar(20), caddr varchar(20), c_pnum integer);
insert into customer values(1,  "Ram", "Ramnagar", 123);
insert into customer values(2,'Raj','Rajnagar',345);
insert into customer values(3,'ayush','jaynagar',456);

create table branch(bid integer primary key, bname varchar(20), baddr varchar(20));
insert into branch values(201, 'A branch', 'Ramnagar');
insert into branch values(202,'B branch', 'Rajnagar');
insert into branch values(203, 'C branch', 'mathikere');

create table account(ac_id integer primary key, ac_type varchar(10), ac_balance varchar(20), cid integer, bid integer, foreign key(cid) references customer(cid), foreign key(bid) references branch(bid));
insert into account values(101,'savings',10000,1,201);
insert into account values(102,'current',20000,2,201);
insert into account values(103,'savings',30000,2,202);
insert into account values(104,'current',25000,3,203);

create table transaction(tid integer primary key, amount integer, ttype varchar(20), ac_id integer, foreign key(ac_id) references account(ac_id));
insert into transaction values(301,5000,'deposit',101);
insert into transaction values(302,2000,'withdrawal',102);
insert into transaction values(303,1000,'withdrawal',101);
insert into transaction values(304,4000,'deposit',103);
insert into transaction values(305,3000,'deposit',101);

#1
select * from customer
where cid in(
select cid from account where ac_type = 'savings'
and cid in( select cid from account where ac_type='current')
);

#2
select branch.* , count(account.bid) as no_of_accounts from account
join branch on account.bid = branch.bid
group by account.bid;

#3
select customer.*, count(transaction.tid) from customer
join account on account.cid = customer.cid
join transaction on transaction.ac_id = account.ac_id
group by customer.cid, customer.cname,customer.caddr
having count(transaction.tid)>=3;

#4
SELECT branch.*, COUNT(account.ac_id) AS num_accounts
FROM branch
JOIN account ON branch.bid = account.bid
GROUP BY branch.bid, branch.bname, branch.baddr
HAVING COUNT(account.ac_id) < (
    SELECT AVG(account_count)
    FROM (
        SELECT bid, COUNT(ac_id) AS account_count
        FROM account
        GROUP BY bid
    ) AS branch_account_counts
);

create table student(usn integer primary key, name varchar(20), gender varchar(20));
insert into student values(101,'Ram','M');
insert into student values(102,'Raj','M');
insert into student values(103,'Radha','F');

create table books(isbn integer primary key, title varchar(20), author varchar(20), publisher varchar(20));
insert into books values(201, 'T1','A1','P1');
insert into books values(202,'T2','A2','P2');
insert into books values(203,'T3','A3','P3');

create table borrows(dates varchar(10), usn integer, isbn integer, foreign key(usn) references student(usn), foreign key(isbn) references books(isbn));
insert into borrows values('1/2/13',101,201);
insert into borrows values('1/2/13',102,202);
insert into borrows values('10/2/13',101,203);
insert into borrows values('10/2/13',103,201);
insert into borrows values('13/2/13',102,203);
#1
select distinct student.name from student
join borrows on borrows.usn = student.usn
where borrows.isbn = 202 or borrows.isbn = 203;

#2
select student.name from student
join borrows on borrows.usn = student.usn
join books on books.isbn = borrows.isbn
where student.gender = 'F' and books.title = 'T1';

#3
select student.*, count(books.isbn) as no_of_books from books
join borrows on borrows.isbn = books.isbn
join student on borrows.usn = student.usn
group by student.usn,student.name,student.gender;