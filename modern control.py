import numpy as np
import matplotlib.pyplot as plt

class StateModel:
    def init(self, A, B, C, D, dt=0.01):
        self.A = np.array(A, dtype=float)
        self.B = np.array(B, dtype=float)
        self.C = np.array(C, dtype=float)
        self.D = np.array(D, dtype=float)
        self.dt = dt
        self._validate()

    def _validate(self):
        rows, cols = self.A.shape
        if rows != cols:
            raise ValueError("Matrix A must be square (n x n).")
        if self.B.shape != (rows, 1):
            raise ValueError("Matrix B must be n x 1.")
        if self.C.shape != (1, rows):
            raise ValueError("Matrix C must be 1 x n.")
        if self.D.shape != (1, 1):
            raise ValueError("Matrix D must be 1 x 1.")

    def simulate(self, input_func, duration=10.0):
        n = self.A.shape[0]
        steps = int(duration / self.dt) + 1
        time_points = np.linspace(0, duration, steps)
        states = np.zeros((n, steps))
        outputs = np.zeros(steps)

        for k in range(steps - 1):
            u_k = input_func(time_points[k])
            state_dot = self.A @ states[:, k] + self.B.flatten() * u_k
            states[:, k + 1] = states[:, k] + self.dt * state_dot
            outputs[k] = self.C @ states[:, k] + self.D.flatten() * u_k

        final_input = input_func(time_points[-1])
        outputs[-1] = self.C @ states[:, -1] + self.D.flatten() * final_input
        return time_points, outputs

    def plot_output(self, time_points, outputs, title="System Response"):
        plt.figure(figsize=(8, 5))
        plt.plot(time_points, outputs, label="Output y(t)")
        plt.title(title)
        plt.xlabel("Time (s)")
        plt.ylabel("Output")
        plt.grid(True)
        plt.legend()
        plt.show()

if name == "main":
    try:
        # Example matrices as part of the question
        A = [[0, 1, 0, 0],
             [-1, -1, 0, 1],
             [0, 0, 0, 1],
             [0, -1, -1, -1]]
        B = [[0], [1], [0], [1]]
        C = [[1, 0, 0, 0]]
        D = [[0]]

        system = StateModel(A, B, C, D)

        def step_input(t):
            return 1.0  # Constant step input

        time_series, system_output = system.simulate(step_input, duration=10.0)
        system.plot_output(time_series, system_output, title="State Space Simulation")

    except Exception as error:
        print("Error:", error)