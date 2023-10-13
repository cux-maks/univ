#pragma warning(disable: 4018)
#pragma warning(disable: 4305)
#pragma warning(disable: 4806)

#define _CRT_SECURE_NO_WARNINGS
#define admin_id "ohm_admin"
#define admin_pw "ohm_716_admin"

#include "non_member.h"
#include <Windows.h>
#include <iostream>
#include "member.h"
#include <fstream>
#include <sstream>
#include <thread>
#include <vector>
#include <ctime>

using std::cout;
using std::cin;
using std::system;

void Delete_Save_Data(); // ��� ������ ����
void Read_Save_Data(vector<member>& m); // ������ �ҷ�����
void Save_Members_Data(vector<member>& m); // ������ ����
void Grading_Members(vector<member>& m); // ȸ�� ��� ����
void Time_Set_Members(vector<member>& m); // ȸ�� �ð� ����
void Time_Pass_Members(vector<member>& m); // ȸ�� ���� �ð� ����
void Time_Set_non_Members(vector<n_member>& m); // ��ȸ�� ���� �ð� ����
void Time_Pass_non_Members(vector<n_member>& n); // ��ȸ�� ���� �ð� ����
void Time_Display_Members(vector<member>& m); // ȸ�� ���� �ð� ���
void Time_Display_Member(string id, vector<member>& m); // ���� ȸ�� ���� �ð� ���
void Time_Display_non_Members(vector<n_member>& n); // ��ȸ�� ���� �ð� ���
void Time_Display_non_Member(string name, vector<n_member>& n); // ��ȸ�� ���� ���� �ð� ���
void Time_Charge_Member(string id, vector<member>& m); // ȸ�� �ð� ����
void Time_Charge_non_Member(string name, vector<n_member>& n); // ��ȸ�� �ð� ����
void Get_Message_to_Admin(); // ī���ͷ� �� �޽��� Ȯ���ϱ�
void Get_Message(string id); // ī���Ϳ��� �� �޽��� Ȯ���ϱ�
void Send_Message_to_Admin(string id); // ī���ͷ� �޽��� ������
void Send_Message(vector<member>& m); // ī���Ϳ��� �޽��� ������
void Display_menu(); // �޴��� ���
void Order_Foods(string id); // ���� �ֹ��ϱ�
void Get_Order(); // �ֹ� Ȯ���ϱ�
void Check_Reservation(vector<member>& m); // ���� Ȯ���ϱ�
void Request_For_Reservation(string id, vector<member>& m); // ���� ��û�ϱ�
void Away(string id, vector<member>& m); // �ڸ����
void Shift(string id, vector<member>& m); // �ڸ� �̵��ϱ�
int Get_Current_Year(); // ���� �⵵ �ҷ�����
int Get_Current_Month(); // ���� �� �ҷ�����
int Get_Current_Day(); // ���� �� �ҷ�����
int Get_Current_Hour(); // ���� �� �ҷ�����
int Get_Current_Min(); // ���� �� �ҷ�����
int Get_Current_Sec(); // ���� �� �ҷ�����
vector<string> split(string str, char Delimiter); // Ư�� ���� ���� string ������
member new_Member(); // �ű� ȸ��
n_member new_Non_Member(); // �ű� ��ȸ��

int main() {

	vector<member> u;
	vector<n_member> n_u;

	Read_Save_Data(u);
	Grading_Members(u);

home:

	string id_input, pw_input;
	bool admin_login = 0;
	bool login = 0;
	int login_cnt = 0;
	int state = 0;

	cout << "---------- ��Ohm PC ----------" << endl;
	cout << "1. �α���" << endl;
	cout << "2. ȸ������" << endl;
	cout << "3. ȸ��Ż��" << endl;
	cout << "4. ��ȸ�� �̿�" << endl;
	cout << "5. ���α׷� ����" << endl;
	cout << ">> ";
	cin >> state;

	/*
	state 1 == �α���
	state 2 == ȸ������
	state 3 == ��ȸ�� �̿�
	state 4 == ���α׷� ����
	else == ��ȿ���� ���� ������
	*/
	if (state == 1) { // �α���

		do {

			system("cls");

			cout << "---------- ��Ohm PC Login ----------" << endl;
			cout << "ID: ";
			cin >> id_input;
			cout << "PW: ";
			cin >> pw_input;

			if (id_input == admin_id && pw_input == admin_pw) { // �������ΰ�?
				cout << "������ �α��� ����." << endl;
				login = 1;
				admin_login = 1;
			}
			else {

				if (u.size() == 0) { // ȸ�� ������ ���� 0�� �� �׳� �α��� ����

					cout << "�α��� ����." << endl;
					login_cnt += 1;
					Sleep(1000);
					system("cls");

				}
				else { // �װ� �ƴ϶�� Ž��

					for (int i = 0; i < u.size(); i++) {

						if (id_input == u[i].GetId() && pw_input == u[i].GetPw()) { // ������ �α��� ����

							cout << "�α��� ����." << endl;
							login = 1;

						}
						else if (i == u.size()) { // �Ȱ��� ���� ������ �α��� ����

							cout << "�α��� ����." << endl;
							login_cnt += 1;
							Sleep(1000);
							system("cls");

						}

					}

				}

			}

			if (login_cnt == 5) { // �α��� 5ȸ ������ ��� ���α׷� ����

				cout << "�α��� 5ȸ ����." << endl;
				cout << "���α׷��� �����մϴ�." << endl;
				Sleep(500);
				return 0;

			}

		} while (login == 0);
	}
	else if (state == 2) { // ȸ������ 

		u.push_back(new_Member());
		Save_Members_Data(u);
		system("cls");
		goto home;

	}
	else if (state == 3) {

		string name, id, pw, buffer;

		cout << "---------- ȸ�� Ż�� ----------" << endl;
		cout << "�̸�: ";
		cin >> name;
		cout << "ID: ";
		cin >> id;
		cout << "PW: ";
		cin >> pw;
		cout << "Ż���Ͻðڽ��ϱ�? (\"Ȯ��\" �Է�)" << endl << ">> ";
		cin >> buffer;

		if (buffer == "Ȯ��") {

			for (int i = 0; i < u.size(); i++) {

				if (u[i].GetName() == name && u[i].GetId() == id) {
					u.erase(u.begin() + i);
					Save_Members_Data(u);
					system("cls");
					goto home;
				}

			}

		}
		else {

			cout << "Ȯ�� �Է� ����." << endl;
			cout << "ȸ�� Ż�� ���." << endl;
			state = 0;
			goto home;

		}

	}
	else if (state == 4) { // ��ȸ�� ���

		n_u.push_back(new_Non_Member());

	}
	else if (state == 5) { // ���α׷� ����

		cout << "���α׷��� �����մϴ�." << endl;
		Time_Pass_Members(u);
		Time_Set_Members(u);
		Save_Members_Data(u);
		return 0;

	}
	else { // �ǵ����� ���� ������

		cout << "�ش� �������� �������� �ʽ��ϴ�." << endl;
		Sleep(500);
		system("cls");
		goto home;

	}

	system("cls");

	login_cnt = 0;

	/*
	admin_login 1 == ������ ȭ��
	state 4 == ��ȸ�� ȭ��
	state 1 == ȸ�� ȭ��
	*/

	if (admin_login == 1) { // ������ �α��� ȭ��

		do {

			int sel;

			cout << "---------- ��Ohm PC ���� ���α׷� ----------" << endl;
			cout << "1. ȸ�� ���� �ð� Ȯ��" << endl;
			cout << "2. �޽��� Ȯ��" << endl;
			cout << "3. �޽��� ������" << endl;
			cout << "4. �ֹ� Ȯ��" << endl;
			cout << "5. ���༮ Ȯ��" << endl;
			cout << "6. ��ȸ�� �ð� ����" << endl;
			cout << "7. �α׾ƿ�" << endl;
			cout << ">> ";
			cin >> sel;

			if (sel == 1) {

				Time_Pass_Members(u);
				Time_Display_Members(u);
				Time_Pass_non_Members(n_u);
				Time_Display_non_Members(n_u);

			}
			else if (sel == 2) {

				Get_Message_to_Admin();

			}
			else if (sel == 3) {

				Send_Message(u);

			}
			else if (sel == 4) {

				Get_Order();

			}
			else if (sel == 5) {

				Check_Reservation(u);

			}
			else if (sel == 7) {

				admin_login = -1;
				goto home;

			}
			else if (sel == 6) {

				string name;

				cout << "������ ȸ�� �̸�: ";
				cin >> name;
				Time_Charge_non_Member(name, n_u);

			}
			else {

				cout << "�ش� �������� �������� �ʽ��ϴ�." << endl;

			}

		} while (admin_login == 1);

	}
	else if (state == 4) { // ��ȸ�� ��� ȭ��

		do {

			int sel;

			cout << "---------- ��Ohm PC ����� ȭ�� ----------" << endl;
			cout << "�غ�ȸ�� �̿��ڴ� ���� �ֹ� �� ���ڸ� ����, �ڸ� �̵� �� ���� �Ǵ� ������, ī���� ����(�޽���) ����� ����Ͻ� �� �����ϴ�." << endl;
			cout << "1. ���� �ð� Ȯ��" << endl;
			cout << "2. �޴� Ȯ��" << endl;
			cout << "3. �α׾ƿ�" << endl;
			cout << ">> ";
			cin >> sel;

			if (sel == 1) {

				string name;

				cout << "<��ȸ�� ���� �ð� Ȯ��>" << endl;
				cout << "�̸�: " << endl;
				cin >> name;

				system("cls");

				Time_Display_non_Member(name, n_u);

			}
			else if (sel == 3) {

				string name;

				cout << "<�α׾ƿ� - ��ȸ���� �ð��� ������� �ʽ��ϴ�.>" << endl;
				cout << "�̸�: " << endl;
				cin >> name;

				for (int i = 0; i < n_u.size(); i++) {

					if (name == n_u[i].GetName()) {

						cout << name << "�� �α׾ƿ� �մϴ�." << endl;
						Sleep(1000);
						system("cls");
						state = 0;
						break;

					}

				}

			}
			else if (sel == 2) {

				cout << "��ȸ���� �޴� Ȯ�θ� �����մϴ�. �ֹ��� ī���Ϳ��� ��Ź�帳�ϴ�." << endl;
				Display_menu();

			}
			else {

				cout << "�ش� �������� �������� �ʽ��ϴ�." << endl;

			}

		} while (state != 0);

	}
	else if (state == 1) { // ȸ�� ��� ȭ��

		do {

			int sel;

			cout << "---------- ��Ohm PC ����� ȭ�� ----------" << endl;
			cout << "1. ���� �ð� Ȯ��" << endl;
			cout << "2. �ð� ����" << endl;
			cout << "3. �޴� Ȯ�� �� �ֹ�" << endl;
			cout << "4. �ڸ� �̵�" << endl;
			cout << "5. ī���Ϳ� �޽��� ������" << endl;
			cout << "6. ī���Ϳ��� �� �޽��� ����" << endl;
			cout << "7. �ڸ���� or �ڸ��� ���ƿ�" << endl;
			cout << "8. �α׾ƿ�" << endl;
			cin >> sel;

			if (sel == 1) {

				Time_Display_Member(id_input, u);

			}
			else if (sel == 3) {

				Order_Foods(id_input);

			}
			else if (sel == 4) {

				Shift(id_input, u);

			}
			else if (sel == 5) {

				Send_Message_to_Admin(id_input);

			}
			else if (sel == 7) {

				Away(id_input, u);

			}
			else if (sel == 8) {

				state = 0;

			}
			else if (sel == 6) {

				Get_Message(id_input);

			}
			else if (sel == 2) {

				Time_Charge_Member(id_input, u);

			}

		} while (state != 0);
	}

	if (admin_login == -1 || state == 0) {

		goto home;

	}

	return 0;

}

void Read_Save_Data(vector<member>& m) {

	ifstream readData("Member_Data.txt");

	if (readData.is_open()) {

		string first_line;
		string date_time;
		getline(readData, first_line);
		int n = stoi(first_line);
		getline(readData, date_time);

		if (n != 0) {

			for (int i = 0; i < n; i++) {

				string str;
				getline(readData, str);

				vector<string> result = split(str, ' ');
				vector<string> left_time = split(result[9], ':');

				member temp(result[0], result[1], result[2], result[3], result[4], stoi(result[5]), result[6], stoi(result[7]), stoi(result[8]), Get_Current_Hour(), Get_Current_Min(), Get_Current_Sec(), stoi(result[10]), stoi(left_time[0]), stoi(left_time[1]), stoi(left_time[2]));

				m.push_back(temp);

			}

		}
		else {

			cout << "There is no data." << endl;

		}

	}
	else {

		cout << "There is no data." << endl;

	}

}

void Delete_Save_Data() {

	ofstream outfile("Member_Data.txt", ios_base::out);

	outfile << 0 << endl;
	outfile << "Warning, Clear." << endl;

}

void Save_Members_Data(vector<member>& m) {

	ofstream outfile("Member_Data.txt", ios_base::out);

	outfile << m.size() << endl;
	outfile << "���α׷� ���� �ð� >> " << Get_Current_Year() << ":" << Get_Current_Month() << ":" << Get_Current_Day() << ":" << Get_Current_Hour() << ":" << Get_Current_Min() << ":" << Get_Current_Sec() << endl;

	for (int i = 0; i < m.size(); i++) {

		string buffer = m[i].GetName();
		buffer += " ";
		buffer += m[i].GetId();
		buffer += " ";
		buffer += m[i].GetPw();
		buffer += " ";
		buffer += m[i].GetTel();
		buffer += " ";
		buffer += m[i].GetEmail();
		buffer += " ";
		buffer += to_string(m[i].GetAge());
		buffer += " ";
		buffer += m[i].GetGrade();
		buffer += " ";
		buffer += to_string(m[i].GetPoint());
		buffer += " ";
		buffer += to_string(m[i].GetPayCnt());
		buffer += " ";
		buffer += to_string(m[i].GetLTH());
		buffer += ":";
		buffer += to_string(m[i].GetLTM());
		buffer += ":";
		buffer += to_string(m[i].GetLTS());
		buffer += " ";
		buffer += to_string(m[i].GetReservation());
		buffer += " ";
		buffer += to_string(m[i].GetSTH());
		buffer += ":";
		buffer += to_string(m[i].GetSTM());
		buffer += ":";
		buffer += to_string(m[i].GetSTS());

		outfile << buffer << endl;

	}

}

void Grading_Members(vector<member>& m) {

	for (int i = 0; i < m.size(); i++) {

		if (m[i].GetPayCnt() > 10) {
			m[i].SetGrade("Silver");
		}
		else if (m[i].GetPayCnt() > 50) {
			m[i].SetGrade("Gold");
		}
		else if (m[i].GetPayCnt() > 100) {
			m[i].SetGrade("Platinum");
		}
		else if (m[i].GetPayCnt() > 200) {
			m[i].SetGrade("Diamond");
		}
		else if (m[i].GetPayCnt() > 400) {
			m[i].SetGrade("Master");
		}
		else if (m[i].GetPayCnt() > 800) {
			m[i].SetGrade("Challenger");
		}

	}

	Save_Members_Data(m);

}

void Time_Set_Members(vector<member>& m) {

	for (int i = 0; i < m.size(); i++) {

		int hour = m[i].GetLTH();
		int min = m[i].GetLTM();
		int sec = m[i].GetLTS();

		if (sec / 60 >= 1) {
			min += sec / 60;
			sec %= 60;
		}

		if (min / 60 >= 1) {
			hour += min / 60;
			min %= 60;
		}

		m[i].SetLTH(hour);
		m[i].SetLTM(min);
		m[i].SetLTS(sec);

	}

	Save_Members_Data(m);

}

void Time_Pass_Members(vector<member>& m) {

	for (int i = 0; i < m.size(); i++) {

		int left_time = (m[i].GetLTH() * 3600) + (m[i].GetLTM() * 60) + m[i].GetLTS();
		int pass_time = ((Get_Current_Hour() * 3600) + (Get_Current_Min() * 60) + Get_Current_Sec()) - ((m[i].GetSTH() * 3600) + (m[i].GetSTM() * 60) + m[i].GetSTS());

		if (pass_time >= left_time && m[i].GetSTH() != -1 && m[i].GetSTM() != -1 && m[i].GetSTS() != -1 && m[i].GetLTH() != -1 && m[i].GetLTM() != -1 && m[i].GetLTS() != -1) {

			m[i].DelSTH();
			m[i].DelSTM();
			m[i].DelSTS();
			m[i].DelLTH();
			m[i].DelLTM();
			m[i].DelLTS();

			cout << m[i].GetName() << "(" << m[i].GetId() << ")���� ��� �ð��� ����Ǿ����ϴ�." << endl;

		}

	}

	Save_Members_Data(m);

}

void Time_Set_non_Members(vector<n_member>& m) {

	for (int i = 0; i < m.size(); i++) {

		int hour = m[i].GetLTH();
		int min = m[i].GetLTM();
		int sec = m[i].GetLTS();

		if (sec / 60 >= 1) {
			min += sec / 60;
			sec %= 60;
		}

		if (min / 60 >= 1) {
			hour += min / 60;
			min %= 60;
		}

		m[i].SetLTH(hour);
		m[i].SetLTM(min);
		m[i].SetLTS(sec);

	}

}

void Time_Pass_non_Members(vector<n_member>& n) {

	for (int i = 0; i < n.size(); i++) {

		int left_time = (n[i].GetLTH() * 3600) + (n[i].GetLTM() * 60) + n[i].GetLTS();
		int pass_time = ((Get_Current_Hour() * 3600) + (Get_Current_Min() * 60) + Get_Current_Sec()) - ((n[i].GetSTH() * 3600) + (n[i].GetSTM() * 60) + n[i].GetSTS());

		if (pass_time >= left_time && n[i].GetSTH() != -1 && n[i].GetSTM() != -1 && n[i].GetSTS() != -1 && n[i].GetLTH() != -1 && n[i].GetLTM() != -1 && n[i].GetLTS() != -1) {

			n[i].DelSTH();
			n[i].DelSTM();
			n[i].DelSTS();
			n[i].DelLTH();
			n[i].DelLTM();
			n[i].DelLTS();

			cout << n[i].GetName() << "���� ��� �ð��� ����Ǿ����ϴ�." << endl;

		}

	}

}

void Time_Display_Members(vector<member>& m) {

	cout << "<ȸ�� ���� �ð�>" << endl;

	for (int i = 0; i < m.size(); i++) {

		int left_time = (m[i].GetLTH() * 3600) + (m[i].GetLTM() * 60) + m[i].GetLTS();
		int pass_time = ((Get_Current_Hour() * 3600) + (Get_Current_Min() * 60) + Get_Current_Sec()) - ((m[i].GetSTH() * 3600) + (m[i].GetSTM() * 60) + m[i].GetSTS());

		int time = left_time - pass_time;

		cout << "id: " << m[i].GetId() << "  " << time / 3600 << ":" << (time % 3600) / 60 << ":" << time % 60 << endl;

	}

}

void Time_Display_Member(string id, vector<member>& m) {

	Time_Pass_Members(m);

	for (int i = 0; i < m.size(); i++) {

		if (id == m[i].GetId() && m[i].GetLTH() != -1) {

			int left_time = (m[i].GetLTH() * 3600) + (m[i].GetLTM() * 60) + m[i].GetLTS();
			int pass_time = ((Get_Current_Hour() * 3600) + (Get_Current_Min() * 60) + Get_Current_Sec()) - ((m[i].GetSTH() * 3600) + (m[i].GetSTM() * 60) + m[i].GetSTS());

			int time = left_time - pass_time;
			cout << left_time << " " << pass_time << " " << time << endl;
			cout << id << "(" << m[i].GetId() << ")���� ���� ��� �ð��� " << time / 3600 << ":" << (time % 3600) / 60 << ":" << time % 60 << " �Դϴ�." << endl;

		}
		else {
			cout << id << "(" << m[i].GetId() << ")���� ���� ��� �ð��� " << 0 << " �Դϴ�." << endl;
		}

	}

	system("pause");
	system("cls");

}

void Time_Display_non_Members(vector<n_member>& n) {

	cout << endl << "<��ȸ�� ���� �ð�>" << endl;

	for (int i = 0; i < n.size(); i++) {

		int left_time = (n[i].GetLTH() * 3600) + (n[i].GetLTM() * 60) + n[i].GetLTS();
		int pass_time = ((Get_Current_Hour() * 3600) + (Get_Current_Min() * 60) + Get_Current_Sec()) - ((n[i].GetSTH() * 3600) + (n[i].GetSTM() * 60) + n[i].GetSTS());

		int time = left_time - pass_time;

		cout << "id: " << n[i].GetName() << "  " << time / 3600 << ":" << (time % 3600) / 60 << time % 60 << endl;

	}

	system("pause");
	system("cls");

}

void Time_Display_non_Member(string name, vector<n_member>& n) {

	for (int i = 0; i < n.size(); i++) {

		if (name == n[i].GetName()) {

			int left_time = (n[i].GetLTH() * 3600) + (n[i].GetLTM() * 60) + n[i].GetLTS();
			int pass_time = ((Get_Current_Hour() * 3600) + (Get_Current_Min() * 60) + Get_Current_Sec()) - ((n[i].GetSTH() * 3600) + (n[i].GetSTM() * 60) + n[i].GetSTS());

			int time = left_time - pass_time;

			cout << name << "���� ���� ��� �ð��� " << time / 3600 << ":" << (time % 3600) / 60 << time % 60 << " �Դϴ�." << endl;

		}

	}

	system("pause");
	system("cls");

}

void Time_Charge_Member(string id, vector<member>& m) {

	int sel;
	string yesorno;

	cout << "---------- �ð� ���� ----------" << endl;
	cout << "1. 1�ð� - 1000��" << endl;
	cout << "2. 2�ð� - 2000��" << endl;
	cout << "3. 3�ð� - 3000��" << endl;
	cout << "4. 4�ð� - 4000��" << endl;
	cout << "5. 5�ð� - 5000��" << endl;
	cout << "6. 6�ð� - 6000��" << endl;
	cout << "7. 12�ð� - 10000��" << endl;
	cout << "����: ";
	cin >> sel;

	for (int i = 0; i < m.size(); i++) {
		if (m[i].GetId() == id) {

			if (m[i].GetSTH() != -1 && m[i].GetSTM() != -1 && m[i].GetSTS() != -1) {
				switch (sel) {
				case 1:

					cout << "����Ʈ�� ����Ͻðڽ��ϱ�? (\"��\" �Ǵ� \"�ƴϿ�\")" << endl;
					cout << ">> ";
					cin >> yesorno;

					if (yesorno == "��") {
						if (m[i].GetPoint() >= 1000) {
							cout << "���� ���� �ݾ�: 0" << endl;
							m[i].SetPoint(m[i].GetPoint() - 1000);
						}
						else {
							cout << "���� ���� �ݾ�: " << (1000 - m[i].GetPoint()) << endl;
							m[i].SetPoint(0);
						}
					}
					m[i].SetLTH(m[i].GetLTH() + 1);
					m[i].SetPoint(m[i].GetPoint() + 10);
					m[i].SetPayCnt(m[i].GetPayCnt() + 1);
					break;
				case 2:

					cout << "����Ʈ�� ����Ͻðڽ��ϱ�? (\"��\" �Ǵ� \"�ƴϿ�\")" << endl;
					cout << ">> ";
					cin >> yesorno;

					if (yesorno == "��") {
						if (m[i].GetPoint() >= 2000) {
							cout << "���� ���� �ݾ�: 0" << endl;
							m[i].SetPoint(m[i].GetPoint() - 2000);
						}
						else {
							cout << "���� ���� �ݾ�: " << (2000 - m[i].GetPoint()) << endl;
							m[i].SetPoint(0);
						}
					}
					m[i].SetLTH(m[i].GetLTH() + 2);
					m[i].SetPoint(m[i].GetPoint() + 20);
					m[i].SetPayCnt(m[i].GetPayCnt() + 1);
					break;
				case 3:

					cout << "����Ʈ�� ����Ͻðڽ��ϱ�? (\"��\" �Ǵ� \"�ƴϿ�\")" << endl;
					cout << ">> ";
					cin >> yesorno;

					if (yesorno == "��") {
						if (m[i].GetPoint() >= 3000) {
							cout << "���� ���� �ݾ�: 0" << endl;
							m[i].SetPoint(m[i].GetPoint() - 3000);
						}
						else {
							cout << "���� ���� �ݾ�: " << (3000 - m[i].GetPoint()) << endl;
							m[i].SetPoint(0);
						}
					}
					m[i].SetLTH(m[i].GetLTH() + 3);
					m[i].SetPoint(m[i].GetPoint() + 30);
					m[i].SetPayCnt(m[i].GetPayCnt() + 1);
					break;
				case 4:

					cout << "����Ʈ�� ����Ͻðڽ��ϱ�? (\"��\" �Ǵ� \"�ƴϿ�\")" << endl;
					cout << ">> ";
					cin >> yesorno;

					if (yesorno == "��") {
						if (m[i].GetPoint() >= 4000) {
							cout << "���� ���� �ݾ�: 0" << endl;
							m[i].SetPoint(m[i].GetPoint() - 4000);
						}
						else {
							cout << "���� ���� �ݾ�: " << (4000 - m[i].GetPoint()) << endl;
							m[i].SetPoint(0);
						}
					}
					m[i].SetLTH(m[i].GetLTH() + 4);
					m[i].SetPoint(m[i].GetPoint() + 40);
					m[i].SetPayCnt(m[i].GetPayCnt() + 1);
					break;
				case 5:

					cout << "����Ʈ�� ����Ͻðڽ��ϱ�? (\"��\" �Ǵ� \"�ƴϿ�\")" << endl;
					cout << ">> ";
					cin >> yesorno;

					if (yesorno == "��") {
						if (m[i].GetPoint() >= 5000) {
							cout << "���� ���� �ݾ�: 0" << endl;
							m[i].SetPoint(m[i].GetPoint() - 5000);
						}
						else {
							cout << "���� ���� �ݾ�: " << (5000 - m[i].GetPoint()) << endl;
							m[i].SetPoint(0);
						}
					}
					m[i].SetLTH(m[i].GetLTH() + 5);
					m[i].SetPoint(m[i].GetPoint() + 50);
					m[i].SetPayCnt(m[i].GetPayCnt() + 1);
					break;
				case 6:

					cout << "����Ʈ�� ����Ͻðڽ��ϱ�? (\"��\" �Ǵ� \"�ƴϿ�\")" << endl;
					cout << ">> ";
					cin >> yesorno;

					if (yesorno == "��") {
						if (m[i].GetPoint() >= 6000) {
							cout << "���� ���� �ݾ�: 0" << endl;
							m[i].SetPoint(m[i].GetPoint() - 6000);
						}
						else {
							cout << "���� ���� �ݾ�: " << (6000 - m[i].GetPoint()) << endl;
							m[i].SetPoint(0);
						}
					}
					m[i].SetLTH(m[i].GetLTH() + 6);
					m[i].SetPoint(m[i].GetPoint() + 60);
					m[i].SetPayCnt(m[i].GetPayCnt() + 1);
					break;
				case 7:

					cout << "����Ʈ�� ����Ͻðڽ��ϱ�? (\"��\" �Ǵ� \"�ƴϿ�\")" << endl;
					cout << ">> ";
					cin >> yesorno;

					if (yesorno == "��") {
						if (m[i].GetPoint() >= 12000) {
							cout << "���� ���� �ݾ�: 0" << endl;
							m[i].SetPoint(m[i].GetPoint() - 12000);
						}
						else {
							cout << "���� ���� �ݾ�: " << (12000 - m[i].GetPoint()) << endl;
							m[i].SetPoint(0);
						}
					}
					m[i].SetLTH(m[i].GetLTH() + 12);
					m[i].SetPoint(m[i].GetPoint() + 120);
					m[i].SetPayCnt(m[i].GetPayCnt() + 1);
					break;
				}
				cout << "������ �Ϸ�Ǿ����ϴ�." << endl;
				system("pause");
				system("cls");
			}
			else {

				m[i].SetSTH(Get_Current_Hour());
				m[i].SetSTM(Get_Current_Min());
				m[i].SetSTS(Get_Current_Sec());
				m[i].SetLTM(0);
				m[i].SetLTS(0);

				switch (sel) {
				case 1:
					cout << "����Ʈ�� ����Ͻðڽ��ϱ�? (\"��\" �Ǵ� \"�ƴϿ�\")" << endl;
					cout << ">> ";
					cin >> yesorno;

					if (yesorno == "��") {
						if (m[i].GetPoint() >= 1000) {
							cout << "���� ���� �ݾ�: 0" << endl;
							m[i].SetPoint(m[i].GetPoint() - 1000);
						}
						else {
							cout << "���� ���� �ݾ�: " << (1000 - m[i].GetPoint()) << endl;
							m[i].SetPoint(0);
						}
					}
					m[i].SetLTH(1);
					m[i].SetPoint(m[i].GetPoint() + 10);
					m[i].SetPayCnt(m[i].GetPayCnt() + 1);
					break;
				case 2:
					cout << "����Ʈ�� ����Ͻðڽ��ϱ�? (\"��\" �Ǵ� \"�ƴϿ�\")" << endl;
					cout << ">> ";
					cin >> yesorno;

					if (yesorno == "��") {
						if (m[i].GetPoint() >= 2000) {
							cout << "���� ���� �ݾ�: 0" << endl;
							m[i].SetPoint(m[i].GetPoint() - 2000);
						}
						else {
							cout << "���� ���� �ݾ�: " << (2000 - m[i].GetPoint()) << endl;
							m[i].SetPoint(0);
						}
					}
					m[i].SetLTH(2);
					m[i].SetPoint(m[i].GetPoint() + 20);
					m[i].SetPayCnt(m[i].GetPayCnt() + 1);
					break;
				case 3:
					cout << "����Ʈ�� ����Ͻðڽ��ϱ�? (\"��\" �Ǵ� \"�ƴϿ�\")" << endl;
					cout << ">> ";
					cin >> yesorno;

					if (yesorno == "��") {
						if (m[i].GetPoint() >= 3000) {
							cout << "���� ���� �ݾ�: 0" << endl;
							m[i].SetPoint(m[i].GetPoint() - 3000);
						}
						else {
							cout << "���� ���� �ݾ�: " << (3000 - m[i].GetPoint()) << endl;
							m[i].SetPoint(0);
						}
					}
					m[i].SetLTH(3);
					m[i].SetPoint(m[i].GetPoint() + 30);
					m[i].SetPayCnt(m[i].GetPayCnt() + 1);
					break;
				case 4:
					cout << "����Ʈ�� ����Ͻðڽ��ϱ�? (\"��\" �Ǵ� \"�ƴϿ�\")" << endl;
					cout << ">> ";
					cin >> yesorno;

					if (yesorno == "��") {
						if (m[i].GetPoint() >= 4000) {
							cout << "���� ���� �ݾ�: 0" << endl;
							m[i].SetPoint(m[i].GetPoint() - 4000);
						}
						else {
							cout << "���� ���� �ݾ�: " << (4000 - m[i].GetPoint()) << endl;
							m[i].SetPoint(0);
						}
					}
					m[i].SetLTH(4);
					m[i].SetPoint(m[i].GetPoint() + 40);
					m[i].SetPayCnt(m[i].GetPayCnt() + 1);
					break;
				case 5:
					cout << "����Ʈ�� ����Ͻðڽ��ϱ�? (\"��\" �Ǵ� \"�ƴϿ�\")" << endl;
					cout << ">> ";
					cin >> yesorno;

					if (yesorno == "��") {
						if (m[i].GetPoint() >= 5000) {
							cout << "���� ���� �ݾ�: 0" << endl;
							m[i].SetPoint(m[i].GetPoint() - 5000);
						}
						else {
							cout << "���� ���� �ݾ�: " << (5000 - m[i].GetPoint()) << endl;
							m[i].SetPoint(0);
						}
					}
					m[i].SetLTH(5);
					m[i].SetPoint(m[i].GetPoint() + 50);
					m[i].SetPayCnt(m[i].GetPayCnt() + 1);
					break;
				case 6:
					cout << "����Ʈ�� ����Ͻðڽ��ϱ�? (\"��\" �Ǵ� \"�ƴϿ�\")" << endl;
					cout << ">> ";
					cin >> yesorno;

					if (yesorno == "��") {
						if (m[i].GetPoint() >= 6000) {
							cout << "���� ���� �ݾ�: 0" << endl;
							m[i].SetPoint(m[i].GetPoint() - 6000);
						}
						else {
							cout << "���� ���� �ݾ�: " << (6000 - m[i].GetPoint()) << endl;
							m[i].SetPoint(0);
						}
					}
					m[i].SetLTH(6);
					m[i].SetPoint(m[i].GetPoint() + 60);
					m[i].SetPayCnt(m[i].GetPayCnt() + 1);
					break;
				case 7:
					cout << "����Ʈ�� ����Ͻðڽ��ϱ�? (\"��\" �Ǵ� \"�ƴϿ�\")" << endl;
					cout << ">> ";
					cin >> yesorno;

					if (yesorno == "��") {
						if (m[i].GetPoint() >= 12000) {
							cout << "���� ���� �ݾ�: 0" << endl;
							m[i].SetPoint(m[i].GetPoint() - 12000);
						}
						else {
							cout << "���� ���� �ݾ�: " << (12000 - m[i].GetPoint()) << endl;
							m[i].SetPoint(0);
						}
					}
					m[i].SetLTH(12);
					m[i].SetPoint(m[i].GetPoint() + 120);
					m[i].SetPayCnt(m[i].GetPayCnt() + 1);
					break;
				}
				cout << "������ �Ϸ�Ǿ����ϴ�." << endl;
				system("pause");
				system("cls");
			}
			
			break;

		}
	}
	
	Save_Members_Data(m);

}

void Time_Charge_non_Member(string name, vector<n_member>& m) {

	int sel;

	cout << "---------- �ð� ���� ----------" << endl;
	cout << "1. 1�ð� - 1000��" << endl;
	cout << "2. 2�ð� - 2000��" << endl;
	cout << "3. 3�ð� - 3000��" << endl;
	cout << "4. 4�ð� - 4000��" << endl;
	cout << "5. 5�ð� - 5000��" << endl;
	cout << "6. 6�ð� - 6000��" << endl;
	cout << "7. 12�ð� - 10000��" << endl;
	cout << "����: ";
	cin >> sel;

	for (int i = 0; i < m.size(); i++) {
		if (m[i].GetName() == name) {

			if (m[i].GetSTH() != -1 && m[i].GetSTM() != -1 && m[i].GetSTS() != -1) {
				switch (sel) {
				case 1:
					m[i].SetLTH(m[i].GetLTH() + 1);
					break;
				case 2:
					m[i].SetLTH(m[i].GetLTH() + 2);
					break;
				case 3:
					m[i].SetLTH(m[i].GetLTH() + 3);
					break;
				case 4:
					m[i].SetLTH(m[i].GetLTH() + 4);
					break;
				case 5:
					m[i].SetLTH(m[i].GetLTH() + 5);
					break;
				case 6:
					m[i].SetLTH(m[i].GetLTH() + 6);
					break;
				case 7:
					m[i].SetLTH(m[i].GetLTH() + 12);
					break;
				}
			}
			else {

				m[i].SetSTH(Get_Current_Hour());
				m[i].SetSTM(Get_Current_Min());
				m[i].SetSTS(Get_Current_Sec());
				m[i].SetLTM(0);
				m[i].SetLTS(0);

				switch (sel) {
				case 1:
					m[i].SetLTH(1);
					break;
				case 2:
					m[i].SetLTH(2);
					break;
				case 3:
					m[i].SetLTH(3);
					break;
				case 4:
					m[i].SetLTH(4);
					break;
				case 5:
					m[i].SetLTH(5);
					break;
				case 6:
					m[i].SetLTH(6);
					break;
				case 7:
					m[i].SetLTH(12);
					break;
				}
				cout << "������ �Ϸ�Ǿ����ϴ�." << endl;
				system("pause");
				system("cls");
			}
			break;
		}
	}

}

void Get_Message_to_Admin() {

	ifstream to_admin("To_Admin.txt");

	if (to_admin.is_open()) {

		string text;

		while (getline(to_admin, text)) {

			cout << text << endl;

		}

	}
	else {

		cout << "There is no data." << endl;

	}

	to_admin.close();

	system("pause");
	system("cls");

}

void Get_Message(string id) {

	ifstream from_admin("From_Admin.txt");

	if (from_admin.is_open()) {

		string text;

		while (getline(from_admin, text)) {

			vector<string> buffer = split(text, ' ');

			if (buffer[0] == id) {

				cout << "admin: " << buffer[1] << endl;

			}

		}

	}
	else {

		cout << "There is no data." << endl;

	}

	from_admin.close();

	system("pause");
	system("cls");

}

void Send_Message_to_Admin(string id) {

	ofstream to_admin("To_Admin.txt", ios_base::app);

	string buffer;

	cout << ">> ";
	cin >> buffer;
	to_admin << "<" << id << "> " << buffer << endl;

	to_admin.close();

	system("pause");
	system("cls");

}

void Send_Message(vector<member>& m) {

	ofstream from_admin("From_Admin.txt", ios_base::app);

	string buffer;
	int select = 0;

	do {

		cout << "���� ������� ���̵� �����ϼ���. (����� -1)" << endl;
		for (int i = 0; i < m.size(); i++) {
			cout << i + 1 << ". " << m[i].GetId() << endl;
		}
		cout << ">> ";
		cin >> select;

		if (select == -1) {
			break;
		}

		cout << "<�޽��� �Է�>" << endl;
		cout << ">> ";
		cin >> buffer;

		from_admin << m[select - 1].GetId() << " " << buffer << endl;

	} while (select != -1);


	from_admin.close();

	system("pause");
	system("cls");

}

void Display_menu() {

	cout << "---------- �޴��� ----------" << endl;
	cout << "<���>" << endl;
	cout << "�����(��)  �����(��)  �Ŷ��  �Ŷ���  �����  �����  ¥�İ�Ƽ  �ʱ���  �Ҵߺ�����  ����Ҵߺ�����  ��«��" << endl;
	cout << "<�Ź�>" << endl;
	cout << "ġŲ����  �Ҵ߸���  ��ġ����  ���Ը���  ������ġ  ġŲ����  �Ҵ߽���  ġŲ�Ҵ߽��Ը���" << endl;
	cout << "<ġŲ>" << endl;
	cout << "�Ѹ���ġŲ  �ݸ���ġŲ  �ݹ�ġŲ  �߰���  (���: �Ķ��̵�, ���, ���, ����, ����)" << endl;
	cout << "<���� - �ַ��� ī���Ϳ��� �ź��� Ȯ�� �� �� 19�� �̻���� �ֹ� �����մϴ�.>" << endl;
	cout << "��ī�ݶ�  ���  ĥ�����̴�  ��������Ʈ  ȯŸ������  ȯŸ���ο���  ���̽�  ó��ó��  ī��  �׶�" << endl;

}

void Order_Foods(string id) {

	ofstream order("order.txt", ios_base::app);

	string buffer;

	Display_menu();

	cout << endl << "�ֹ� ������ �����ּ���." << endl << ">> ";
	cin >> buffer;

	order << id << buffer << endl;

	order.close();

	system("pause");
	system("cls");

}

void Get_Order() {

	ifstream order("Order.txt");

	string buffer;

	while (getline(order, buffer)) {

		cout << buffer << endl;

	}

	order.close();

	ofstream clean("Order.txt", ios_base::out);

	string clear = "";

	clean << clear;

	clean.close();

	system("pause");
	system("cls");

}

void Check_Reservation(vector<member>& m) {

	ifstream reservation("Reservation.txt");

	string buffer;

	while (getline(reservation, buffer)) {

		int accept;
		cout << buffer << endl;
		cout << "���� �㰡 �Ͻðڽ��ϱ�?(yes = 1, no = 0)" << endl << ">> ";
		cin >> accept;
		if (accept == 1) {
			vector<string> result = split(buffer, ' ');
			for (int i = 0; i < m.size(); i++) {

				if (m[i].GetName() == result[0] && m[i].GetId() == result[1]) {
					m[i].SetReservation(stoi(result[2]));
					cout << "������ �Ϸ�Ǿ����ϴ�." << endl;
					break;
				}

			}
		}
		else {

			cout << "������ �ź��Ͽ����ϴ�." << endl;

		}

	}

	reservation.close();

	string clean = "";
	ofstream reservation_end("Reservation.txt", ios_base::out);
	reservation_end << clean;
	reservation_end.close();

	system("pause");
	system("cls");
	Save_Members_Data(m);

}

void Request_For_Reservation(string id, vector<member>& m) {

	ofstream reservation("Reservation.txt", ios_base::out);

	string buffer = "";
	string name, num;

	cout << "��û���� �̸��� �¼� ��ȣ�� �Է��Ͻÿ�." << endl;
	cout << "�̸�: ";
	cin >> name;
	cout << "�¼� ��ȣ: ";
	cin >> num;

	buffer += name;
	buffer += " ";
	buffer += num;

	reservation << buffer << endl;

	reservation.close();

	system("pause");
	system("cls");

}

void Shift(string id, vector<member>& m) {

	int ok = 0;

	while (ok == 0) {

		int num;

		cout << "�ڸ� ��ȣ: ";
		cin >> num;

		for (int i = 0; i < m.size(); i++) {

			if (num == m[i].GetReservation()) {

				cout << "�̹� ������̰ų� ����� �ڸ� �Դϴ�." << endl;
				cout << "�ٸ� �ڸ��� �������ּ���." << endl;
				Sleep(1000);
				system("cls");
				break;

			}

			if (i >= m.size() - 1) {

				m[i].SetReservation(num);
				cout << "�ڸ��̵��� �Ϸ�Ǿ����ϴ�." << endl;
				Sleep(1000);
				system("cls");
				ok = 1;

			}

		}
	}

}

void Away(string id, vector<member>& m) {

	for (int i = 0; i < m.size(); i++) {
		if (id == m[i].GetId()) {
			if (m[i].GetAway() == 0) {
				cout << "�ڸ�������� �����մϴ�." << endl;
				m[i].SetAway(1);
				system("pause");
				system("cls");
			}
			else {
				cout << "��������� �����մϴ�." << endl;
				m[i].SetAway(0);
				system("pause");
				system("cls");
			}
		}
	}

}

member new_Member() {

	string name, id, pw, email, tel;
	int age;

	cout << "---------- ȸ������ ----------" << endl;
	cout << "ID: ";
	cin >> id;
	cout << "PW: ";
	cin >> pw;
	cout << "�̸�: ";
	cin >> name;
	cout << "����: ";
	cin >> age;
	cout << "��ȭ��ȣ: ";
	cin >> tel;
	cout << "e-mail: ";
	cin >> email;

	member temp(name, id, pw, tel, email, age);

	cout << "ȸ�����Կ� �����߽��ϴ�." << endl;

	return temp;

}

n_member new_Non_Member() {

	string name, tel;
	int age;

	cout << "---------- ��ȸ�� �ʼ� ���� �Է� ----------" << endl;
	cout << "�̸�: ";
	cin >> name;
	cout << "����: ";
	cin >> age;
	cout << "��ȭ��ȣ: ";
	cin >> tel;

	n_member temp(name, tel, age, Get_Current_Hour(), Get_Current_Min(), Get_Current_Sec());

	return temp;

}

vector<string> split(string str, char Delimiter) {
	istringstream iss(str);
	string buffer;

	vector<string> result;

	while (getline(iss, buffer, Delimiter)) {
		result.push_back(buffer);
	}

	return result;
}

int Get_Current_Year() {

	time_t curTime = time(NULL);
	struct tm* t;
	t = localtime(&curTime);
	return (t->tm_year) + 1900;

}

int Get_Current_Month() {

	time_t curTime = time(NULL);
	struct tm* t;
	t = localtime(&curTime);
	return (t->tm_mon) + 1;

}

int Get_Current_Day() {

	time_t curTime = time(NULL);
	struct tm* t;
	t = localtime(&curTime);
	return t->tm_mday;

}

int Get_Current_Hour() {

	time_t curTime = time(NULL);
	struct tm* t;
	t = localtime(&curTime);
	return t->tm_hour;

}

int Get_Current_Min() {

	time_t curTime = time(NULL);
	struct tm* t;
	t = localtime(&curTime);
	return t->tm_min;

}

int Get_Current_Sec() {

	time_t curTime = time(NULL);
	struct tm* t;
	t = localtime(&curTime);
	return t->tm_sec;

}