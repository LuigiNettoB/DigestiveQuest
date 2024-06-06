/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package br.com.digestivequestgame.controller;

import br.com.digestivequestgame.dao.Conexao;
import br.com.digestivequestgame.dao.LoginDAO;
import br.com.digestivequestgame.view.TelaCadastro;
import br.com.digestivequestgame.view.TelaLogin;
import java.sql.Connection;
import java.sql.SQLException;

/**
 *
 * @author AMD
 */
public class LoginController {
    
    
    public void cadastroUsuario(TelaCadastro view) throws SQLException {
        Connection conexao = new Conexao(). getConnection();
        LoginDAO cadastro = new LoginDAO();
        cadastro.cadastrarUsuario(view.getCadastroNomeField().getText(), view.getCadastroEmailField().getText(), view.getCadastroAnoField().getText(), view.getCadastroSerieField().getText(), view.getCadastroPasswordField().getText());
    }
    
    
    public void loginUsuario(TelaLogin view) throws SQLException {
        Connection conexao = new Conexao(). getConnection();
        LoginDAO login = new LoginDAO();
        login.login(view.getLoginEmailField().getText(), view.getLoginPasswordField().getText());
    }
}