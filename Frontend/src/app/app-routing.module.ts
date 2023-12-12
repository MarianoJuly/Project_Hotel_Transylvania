import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { ModalComponent } from './components/modal/modal.component';
import { FirstComponentComponent } from './components/formularios/registrar-cliente/first-component.component';
import { HomeComponent } from './components/home/home.component';
import { RegistrarFuncionariosComponent } from './components/formularios/registrar-funcionarios/registrar-funcionarios.component';
import { LoginComponent } from './components/formularios/login/login.component';
import { HotelModalComponent } from './components/hotel-modal/hotel-modal.component';
import { RegistrarHotelComponent } from './components/formularios/registrar-hotel/registrar-hotel.component';

const routes: Routes = [
  {path: 'modalDatas', component: ModalComponent},
  {path: 'formulario', component: FirstComponentComponent},
  {path: 'formularioFuncionario', component: RegistrarFuncionariosComponent},
  {path: 'home',component: HomeComponent},
  {path: 'login', component: LoginComponent },
  {path: 'listaHotel', component: HotelModalComponent },
  {path: 'registrarHotel', component: RegistrarHotelComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
