public class BinSort {
	static int binSearch(int target, int[] list) {
		int left = 0;
		int right = list.length - 1;
		int p = -1;

		while (right >= left) {
			p = (right + left) / 2;
			if (target < list[p]) {
				right = p - 1;
			} else if (target > list[p]) {
				left = p + 1;
			} else {
				return p;
			}
		}

		return p;
	}

	static int binSearchLeft(int target, int[] list) {
		int left = 0;
		int right = list.length - 1;
		int p;
		int result = -1;

		while (right >= left) {
			p = (right + left) / 2;
			if (target < list[p]) {
				right = p - 1;
			} else if (target > list[p]) {
				result = p;
				left = p + 1;
			} else {
				return p;
			}
		}

		// points less than target; -1: less than the first
		return result;
	}

	static int binSearchRight(int target, int[] list) {
		int left = 0;
		int right = list.length - 1;
		int p;
		int result = -1;

		while (right >= left) {
			p = (right + left) / 2;
			if (target < list[p]) {
				result = p;
				right = p - 1;
			} else if (target > list[p]) {
				left = p + 1;
			} else {
				return p;
			}
		}

		// points greater than target; -1: greater than last
		return result;
	}

	public static void main(String[] args) {
		int[] samples = { 2, 4, 6, 8, 10, 12 };

		for (int i = 1; i <= 13; i += 2) {
			int std = binSearch(i, samples);
			int r = binSearchRight(i, samples);
			int l = binSearchLeft(i, samples);
//			System.out.println("" + i + "=> std:" + std + " Left:" + l + " Right:" + r);
			System.out.println("" + i + "=> std:" + samples[std] + " Left:" + ((l >= 0) ? samples[l] : "L") + " Right:"
					+ ((r >= 0) ? samples[r] : "R"));
		}
	}

}
