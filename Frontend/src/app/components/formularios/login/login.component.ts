import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { ControleFuncService } from 'src/services/controle-func.service';
import { ControleService } from 'src/services/controle.service';
import { MessagesService } from 'src/services/messages.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit{

  formulario!: FormGroup;

  constructor(private serviceFunc: ControleFuncService,   private formBuilder: FormBuilder, private mensagens: MessagesService){}

  ngOnInit(): void {
    this.criaForm();
  }

  async criaForm(){
    this.formulario = new FormGroup({
      cpf: new FormControl('', [Validators.required]),
      senha: new FormControl('', [Validators.required])
    });
  }

  async submit() {
    console.log("validação1")
    if(this.formulario.invalid){
      this.mensagens.add("Não foi possivel salvar o formulario");
      return;
    }else{
      console.log("validação2")
      this.serviceFunc.loging(this.formulario.value).subscribe();
      this.mensagens.add("Formulario Salvo com sucesso");
    }
  }

  get cpf(){
    return this.formulario.get('cpf')!;
  }

  get senha(){
    return this.formulario.get('senha')!;
  }

}
