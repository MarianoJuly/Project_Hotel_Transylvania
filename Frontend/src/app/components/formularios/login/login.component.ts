import { Component } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { MessagesService } from 'src/services/messages.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {

  formulario!: FormGroup;

  constructor(private formBuilder: FormBuilder, private mensagens: MessagesService){}

  ngOnInit(): void {
    this.criaForm();
  }

  async criaForm(){
    this.formulario = new FormGroup({
      email: new FormControl(this.token.email, [Validators.required]),
      senha: new FormControl(this.token.senha, [Validators.required])
    });
  }

  token: any = {
    email: '',
    senha: ''
  }

  async submit() {
    if(this.formulario.invalid){
      this.mensagens.add("Não foi possivel salvar o formulario");
      return;
    }else{
      this.mensagens.add("Formulario Salvo com sucesso");
    }
  }

  get email(){
    return this.formulario.get('email')!;
  }

  get senha(){
    return this.formulario.get('senha')!;
  }



}
