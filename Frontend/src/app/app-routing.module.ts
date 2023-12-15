import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { FirstComponentComponent } from './components/formularios/registrar-cliente/first-component.component';
import { HomeComponent } from './components/home/home.component';
import { LoginComponent } from './components/formularios/login/login.component';
import { HotelModalComponent } from './components/hotel-modal/hotel-modal.component';
import { RegistrarHotelComponent } from './components/formularios/registrar-hotel/registrar-hotel.component';
import { ModalFuncionarioComponent } from './components/modal-funcionario/modal-funcionario.component';
import { RegistrarFuncionariosComponent } from './components/formularios/funcionario/registrar-funcionarios/registrar-funcionarios.component';
import { EditarFuncionarioComponent } from './components/formularios/funcionario/editar-funcionario/editar-funcionario.component';

const routes: Routes = [
  {path: 'modalDatas', component: ModalFuncionarioComponent},
  {path: 'formulario', component: FirstComponentComponent},
  {path: 'formularioFuncionario', component: RegistrarFuncionariosComponent},
  {path: 'home',component: HomeComponent},
  {path: 'login', component: LoginComponent },
  {path: 'listaHotel', component: HotelModalComponent },
  {path: 'registrarHotel', component: RegistrarHotelComponent},
  {path: 'editar/:cpf', component: EditarFuncionarioComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
