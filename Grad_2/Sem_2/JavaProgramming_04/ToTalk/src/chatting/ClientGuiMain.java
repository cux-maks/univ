package chatting;

import java.net.InetAddress;
import java.net.UnknownHostException;

public class ClientGuiMain {
	public static void main(String[] args) {
		try {
			InetAddress ia = InetAddress.getLocalHost();
			String ip_str = ia.toString();
			String ip = ip_str.substring(ip_str.indexOf("/") + 1);
//			System.out.println("test" + ip);
			new ClientGui(ip, 5420);
		} catch (UnknownHostException e) {
			e.printStackTrace();
		}
	}
}