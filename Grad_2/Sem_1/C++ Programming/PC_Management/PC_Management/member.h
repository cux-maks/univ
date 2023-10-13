#pragma warning(disable: 26495)
#pragma once

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class member {

	string name, id, pw, email, tel, grade;
	int age, point, pay_cnt;
	int left_time_hour, left_time_min, left_time_sec; // 남은 시간
	int start_time_hour, start_time_min, start_time_sec; // 로그인 시간
	int reservation;
	bool away = 0;

public:

	member() {}
	member(string _name, string _id, string _pw, string _tel, string _email, int _age, string _grade = "Bronze", int _point = 0, int _pay_cnt = 0, int _start_time_hour = -1, int _start_time_min = -1, int _start_time_sec = -1, int _reservation = -1, int _left_time_hour = -1, int _left_time_min = -1, int _left_time_sec = -1) {
		name = _name;
		tel = _tel;
		id = _id;
		pw = _pw;
		email = _email;
		age = _age;
		grade = _grade;
		point = _point;
		pay_cnt = _pay_cnt;
		start_time_hour = _start_time_hour;
		start_time_min = _start_time_min;
		start_time_sec = _start_time_sec;
		left_time_hour = _left_time_hour;
		left_time_min = _left_time_min;
		left_time_sec = _left_time_sec;
		reservation = _reservation;
	}
	member(const member& u) {
		name = u.name;
		tel = u.tel;
		id = u.id;
		pw = u.pw;
		email = u.email;
		age = u.age;
		grade = u.grade;
		point = u.point;
		pay_cnt = u.pay_cnt;
		start_time_hour = u.start_time_hour;
		start_time_min = u.start_time_min;
		start_time_sec = u.start_time_sec;
		left_time_hour = u.left_time_hour;
		left_time_min = u.left_time_min;
		left_time_sec = u.left_time_sec;
		reservation = u.reservation;
	}
	~member() {
		name.clear();
		tel.clear();
		id.clear();
		pw.clear();
		email.clear();
		grade.clear();
		start_time_hour = -1;
		start_time_min = -1;
		start_time_sec = -1;
		left_time_hour = -1;
		left_time_min = -1;
		left_time_sec = -1;
		reservation = -1;
		pay_cnt = 0;
		age = 0;
		point = 0;
	}

	void DispInfo() {
		cout << "이름: " << name << endl;
		cout << "나이: " << age << endl;
		cout << "ID: " << id << endl;
		cout << "PW: " << pw << endl;
		cout << "회원 등급: " << grade << endl;
		cout << "적립 포인트: " << point << endl;
		cout << "Tel: " << tel << endl;
		cout << "E-mail: " << email << endl;
		cout << "남은 시간: " << left_time_hour << ":" << left_time_min << ":" << left_time_sec << endl;
		cout << "현재 상태: " << (away ? "사용중" : "자리비움") << endl;
	}

	string GetName() { return name; }
	string GetTel() { return tel; }
	string GetId() { return id; }
	string GetPw() { return pw; }
	string GetEmail() { return email; }
	string GetGrade() { return grade; }
	int GetAge() { return age; }
	int GetPoint() { return point; }
	int GetPayCnt() { return pay_cnt; }
	int GetSTH() { return start_time_hour; }
	int GetSTM() { return start_time_min; }
	int GetSTS() { return start_time_sec; }
	int GetLTH() { return left_time_hour; }
	int GetLTM() { return left_time_min; }
	int GetLTS() { return left_time_sec; }
	int GetReservation() { return reservation; }
	bool GetAway() { return away; }

	void SetId(string _id) { id = _id; }
	void SetPw(string _pw) { pw = _pw; }
	void SetEmail(string _email) { email = _email; }
	void SetName(string _name) { name = _name; }
	void SetTel(string _tel) { tel = _tel; }
	void SetGrade(string _grade) { grade = _grade; }
	void SetAge(int _age) { age = _age; }
	void SetPoint(int _point) { point = _point; }
	void SetPayCnt(int _pay_cnt) { pay_cnt = _pay_cnt; }
	void SetSTH(int _start_time_hour) { start_time_hour = _start_time_hour; }
	void SetSTM(int _start_time_min) { start_time_min = _start_time_min; }
	void SetSTS(int _start_time_sec) { start_time_sec = _start_time_sec; }
	void SetLTH(int _left_time_hour) { left_time_hour = _left_time_hour; }
	void SetLTM(int _left_time_min) { left_time_min = _left_time_min; }
	void SetLTS(int _left_time_sec) { left_time_sec = _left_time_sec; }
	void SetReservation(int _reservation) { reservation = _reservation; }
	void SetAway(bool _away) { away = _away; }

	void DelId() { id.clear(); }
	void DelPw() { pw.clear(); }
	void DelEmail() { email.clear(); }
	void DelName() { name.clear(); }
	void DelTel() { tel.clear(); }
	void DelGrade() { grade.clear(); }
	void DelAge() { age = 0; }
	void DelPoint() { point = 0; }
	void DelPayCnt() { pay_cnt = 0; }
	void DelAway() { away = 0; }
	void DelSTH() { start_time_hour = -1; }
	void DelSTM() { start_time_hour = -1; }
	void DelSTS() { start_time_sec = -1; }
	void DelLTH() { left_time_hour = -1; }
	void DelLTM() { left_time_min = -1; }
	void DelLTS() { left_time_sec = -1; }
	void DelReservation() { reservation = -1; }

};