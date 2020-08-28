import java.util.Random;

public class Evolution {
	int max_popu = 10;
	double sum_error, parent1, parent2;
	Agent p1, p2;
	Agent[] population;
	double[] error_values;
	Random r = new Random();
	
	public Evolution() {
		population = new Agent[max_popu];
		for (int i = 0; i<population.length; i++) {
			population[i] = new Agent();
		}
		
		error_values = new double[max_popu];
		for (int i = 0; i<max_popu; i++) {
			error_values[i] = population[i].error();
			sum_error += error_values[i];
		}
		
		double[] again_select_prob = new double[max_popu];
		for (int i = 0; i<error_values.length; i++) {
			again_select_prob[i] = error_values[i] / sum_error;
		}
	}
	
	public String[] sum_two(int cut, String[] a, String[] b) {
		String[] sum_array = new String[a.length];
		for(int i = 0; i < cut; i++) {
			sum_array[i] = a[i];
		}
		for(int j = b.length - 1; j >= cut; j--) {
			sum_array[j] = b[j];
		}
		return sum_array;
	}
	
	public Agent sel_per1(){
		double acc = error_values[0];
		p1 = population[0];
		for(int i = 1; i<error_values.length; i++) {
			if(error_values[i] > acc) {
				acc = error_values[i];
				p1 = population[i];
			}
		}
		parent1 = acc;
		return p1;
	}	
	
	public Agent sel_per2(){
		double acc = error_values[0];
		p2 = population[0];
		for(int i =  1; i<error_values.length; i++) {
			if(error_values[i] > acc && error_values[i] < parent1) {
				acc = error_values[i];
				p2 = population[i];
			}
		}
		parent2 = acc;
		return p2;
	}
	
	public String[] crossover(Agent p1, Agent p2) {
		int cutoff = r.nextInt(max_popu);
		String[] child = sum_two(cutoff, p1.all_history, p2.all_history);
		return child;
	}
	
	public Agent create_new_child() {
		Agent parent1 = sel_per1();
		Agent parent2 = sel_per2();
		Agent child = new Agent();;
		String[] child_all_his = crossover(parent1, parent2);
		child.set_Gene(child_all_his);
		return child;
	}
	
	public void create_new_popu() {
		Agent[] new_popu = new Agent[max_popu];
		for(int news = 0; news < max_popu - 1; news++) {
			new_popu[news] = create_new_child();
		}
		
		population = new_popu;
		new_popu[max_popu - 1] = p1;
		
		double[] error_values = new double[max_popu];
		for (int i = 0; i<max_popu; i++) {
			error_values[i] = population[i].error();
			sum_error += error_values[i];
		}
	}
	
	public Agent evolve(int n_times) {
		for(int turn = 0; turn < n_times; turn++) {
			create_new_popu();
		}
		p1.show_map();
		return p1;
	}

}