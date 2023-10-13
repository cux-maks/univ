#pragma warning(disable: 26495)
#pragma once

#include <iostream>
#include <string>

using namespace std;

class n_member {

	string name, tel;
	int age;
	int left_time_hour, left_time_min, left_time_sec;
	int start_time_hour, start_time_min, start_time_sec;

public:

	n_member() {}
	n_member(string _name, string _tel, int _age, int _sth, int _stm, int _sts, int _lth = 0, int _ltm = 0, int _lts = 0) {
		name = _name;
		tel = _tel;
		age = _age;
		left_time_hour = _lth;
		left_time_min = _ltm;
		left_time_sec = _lts;
		start_time_hour = _sth;
		start_time_min = _stm;
		start_time_sec = _sts;
	}
	n_member(const n_member& u) {
		name = u.name;
		tel = u.tel;
		age = u.age;
		left_time_hour = u.left_time_hour;
		left_time_min = u.left_time_min;
		left_time_sec = u.left_time_sec;
		start_time_hour = u.start_time_hour;
		start_time_min = u.start_time_min;
		start_time_sec = u.start_time_sec;
	}
	~n_member() {
		name.clear();
		tel.clear();
		start_time_hour = -1;
		start_time_min = -1;
		start_time_sec = -1;
		left_time_hour = -1;
		left_time_min = -1;
		left_time_sec = -1;
		age = 0;
	}

	virtual void DispInfo() {
		cout << "이름: " << name << endl;
		cout << "나이: " << age << endl;
		cout << "Tel: " << tel << endl;
	}

	string GetName() { return name; }
	string GetTel() { return tel; }
	int GetAge() { return age; }
	int GetSTH() { return start_time_hour; }
	int GetSTM() { return start_time_min; }
	int GetSTS() { return start_time_sec; }
	int GetLTH() { return left_time_hour; }
	int GetLTM() { return left_time_min; }
	int GetLTS() { return left_time_sec; }

	void SetName(string _name) { name = _name; }
	void SetTel(string _tel) { tel = _tel; }
	void SetAge(int _age) { age = _age; }
	void SetSTH(int _start_time_hour) { start_time_hour = _start_time_hour; }
	void SetSTM(int _start_time_min) { start_time_min = _start_time_min; }
	void SetSTS(int _start_time_sec) { start_time_sec = _start_time_sec; }
	void SetLTH(int _left_time_hour) { left_time_hour = _left_time_hour; }
	void SetLTM(int _left_time_min) { left_time_min = _left_time_min; }
	void SetLTS(int _left_time_sec) { left_time_sec = _left_time_sec; }

	
	void DelName() { name.clear(); }
	void DelTel() { tel.clear(); }
	void DelAge() { age = 0; }
	void DelSTH() { start_time_hour = -1; }
	void DelSTM() { start_time_hour = -1; }
	void DelSTS() { start_time_sec = -1; }
	void DelLTH() { left_time_hour = -1; }
	void DelLTM() { left_time_min = -1; }
	void DelLTS() { left_time_sec = -1; }

};