import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class Agent {
	int x, y, acc, total_move, step_counter, x_target, y_target;
	String[] all_history;
	int [] all_y_his;
	int [] all_x_his;
	int[][] map = new int [8][8];
	String[] possible_moves = {};
	Random random = new Random();
	
	public Agent() {
		all_history = new String[16];
		all_x_his = new int[16];
		all_x_his[0] = 0;
		all_y_his = new int[16];
		all_y_his[0] = 0;
		x = 0;
		y = 0;
		x_target = 7;
		y_target = 7;
		step_counter = 0;
		total_move = 15;
		possible_moves = new String[]{"UP", "LEFT", "RIGHT", "DOWN"};
		create_map();
		move();
		error();
	}
	
	/*public void print() {
		for(int i = 0; i<all_x_his.length; i++) {
			System.out.println(all_x_his[i]);
		}
	}*/
	
	public int[] add_new_ele(int[] old_list, int x) {
		int [] new_list = new int[old_list.length + 1];
		for (int i = 0; i<old_list.length; i++) {
			new_list[i] = old_list[i];
		}
		new_list[old_list.length] = x;
		old_list = new_list;
		return old_list;
	}

	public void create_map() {
		map[0][0] = 1;
		map[x_target][y_target] = 2;
		for(int i = 1; i<7; i++) {
			for(int j = 1; j<7; j++) {
				map[i][j] = 0;
			}
		}
	}
	
	public void show_map() {
		for(int i = 0; i<8; i++) {
			for(int j = 0; j<8; j++) {
				System.out.print(map[i][j]);
				
			}
			System.out.println();
		}
		System.out.println();
		for(int j = 0; j < total_move; j++) {
			System.out.print(all_history[j] + " ");
		}
		System.out.println();
	}
	
	public void mark_xy() {
		map[y][x] = 1;
	}
	
	public void UP() {
		all_history[step_counter] = "UP";
		step_counter++;
		if(y < 7){
			y++;
		}
		all_y_his[step_counter] = y;
	}
	
	public void LEFT() {
		all_history[step_counter] = "LEFT";
		step_counter++;
		if(x > 0){
			x--;
		}
		all_x_his[step_counter] = x;
	}
	
	public void RIGHT() {
		all_history[step_counter] = "RIGHT";
		step_counter++;
		if(x < 7){
			x++;
		}
		all_x_his[step_counter] = x;
	}
	
	public void decision() {
		int num = random.nextInt(3);
		switch(num) {
			case 0:
				UP();
				break;
			case 1:
				LEFT();
				break;
			case 2:
				RIGHT();
				break;
		}
	}
	
	public void move() {
		for(int i = 0; i < total_move; i++) {
			decision();
			//add_new_ele(all_x_his, x);
			//add_new_ele(all_y_his, y);
			mark_xy();
		}
	}
	
	public double error() {
        double error_X = (x_target - all_x_his[all_x_his.length - 1]);
        double error_Y = (y_target - all_y_his[all_y_his.length - 1]);
        double error = 1/(1 + Math.sqrt(error_X * error_X + error_Y * error_Y));
        return error;
	}
	
	public void set_Gene(String[] new_gene) {
		all_history = new_gene;
	}
}