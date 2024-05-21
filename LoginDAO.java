/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package br.com.digestivequestgame.dao;

import br.com.digestivequestgame.model.Login;
import br.com.digestivequestgame.view.TelaMenu;
import br.com.digestivequestgame.view.TelaMenuProf;
import java.awt.Component;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import javax.swing.JOptionPane;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author AMD
 */
public class LoginDAO {
    public void cadastrarUsuario(String nome, String email, String ano, String serie, String senha) throws SQLException {
        Connection conexao = new Conexao().getConnection();
        String sql = "INSERT INTO usuario (nomeUsuario,emailUsuario,anoUsuario,serieUsuario,senhaUsuario)VALUES ('"+nome+"','"+email+"','"+ano+"','"+serie+"', '"+senha+"' )";
        PreparedStatement statement = conexao.prepareStatement(sql);
        statement.execute();
        conexao.close();
    }
    
    public void login(String email, String senha) throws SQLException{
        Connection conexao = new Conexao().getConnection();
        String sql = "SELECT emailUsuario, senhaUsuario FROM usuario WHERE emailUsuario = '"+email+"' AND senhaUsuario = '"+senha+"'  ";
        PreparedStatement statement = conexao.prepareStatement(sql);
        ResultSet rs = statement.executeQuery();
        
        if (rs.next()) {
            System.out.println("Possui");
            if (email.contains("@pro")) {
                Component parentComponent = null;
                JOptionPane.showMessageDialog(parentComponent, "Bem vindo Professor !"); 
                TelaMenuProf telaMenuProf = new TelaMenuProf();
                telaMenuProf.setVisible(true);
            } else {
                TelaMenu telaDeMenu = new TelaMenu();
                telaDeMenu.setVisible(true);
            }
        } else {
            System.out.println("Nao Possui");
            Component parentComponent = null;
            JOptionPane.showMessageDialog(parentComponent, "Usuário ou senha não existem !");
        }
        conexao.close();
    }
    
    
}
