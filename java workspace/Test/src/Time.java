
class Time {
		
	int hour, minute;
	double second;
	
	public Time() {
		this.hour = 0;
		this.minute = 0;
		this.second = 0.0;
	}
		
	public Time(int hour, int minute, double second) {
		this.hour = hour;
		this.minute = minute;
		this.second = second;
	}
	
	public void printTime() {
		System.out.println(hour + ":" + minute + ":" + (int)second);
	}
		}
