import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Login {
    public static void main(String[] args) {
        // Crear el marco principal
        JFrame frame = new JFrame("Aplicación con Pestaña de Login");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);

        // Crear el componente de pestañas
        JTabbedPane tabbedPane = new JTabbedPane();

        // Panel de Login
        JPanel loginPanel = new JPanel();
        loginPanel.setLayout(new GridBagLayout());

        // Componentes del Login
        JLabel userLabel = new JLabel("Usuario:");
        JTextField userField = new JTextField(15);

        JLabel passLabel = new JLabel("Contraseña:");
        JPasswordField passField = new JPasswordField(15);

        JButton loginButton = new JButton("Iniciar Sesión");

        // Configuración del layout
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 5, 5, 5); // Espaciado entre componentes
        gbc.gridx = 0;
        gbc.gridy = 0;
        loginPanel.add(userLabel, gbc);

        gbc.gridx = 1;
        gbc.gridy = 0;
        loginPanel.add(userField, gbc);

        gbc.gridx = 0;
        gbc.gridy = 1;
        loginPanel.add(passLabel, gbc);

        gbc.gridx = 1;
        gbc.gridy = 1;
        loginPanel.add(passField, gbc);

        gbc.gridx = 1;
        gbc.gridy = 2;
        loginPanel.add(loginButton, gbc);

        // Acción para el botón de login
        loginButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String username = userField.getText();
                String password = new String(passField.getPassword());

                if (username.equals("admin") && password.equals("1234")) {
                    JOptionPane.showMessageDialog(frame, "¡Inicio de sesión exitoso!", "Éxito", JOptionPane.INFORMATION_MESSAGE);
                } else {
                    JOptionPane.showMessageDialog(frame, "Usuario o contraseña incorrectos", "Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        });

        // Agregar el panel de login al componente de pestañas
        tabbedPane.addTab("Login", loginPanel);

        // Panel de ejemplo adicional (opcional)
        JPanel anotherTab = new JPanel();
        anotherTab.add(new JLabel("Otra pestaña"));
        tabbedPane.addTab("Otra Pestaña", anotherTab);

        // Agregar las pestañas al marco principal
        frame.add(tabbedPane);

        // Mostrar el marco
        frame.setVisible(true);
    }
}
