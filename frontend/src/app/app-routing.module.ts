import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';


const routes: Routes = [
  {path : '', redirectTo : 'login', pathMatch : 'full'},
  // {path : 'dashboard', children :
  // [
  //   {path : '', redirectTo: 'patient', pathMatch: 'full'},
  //   {path : 'patient', component: PatientComponent},
  //   {path : 'doctor', component: DoctorComponent},
  //   {path : 'doctor/:id', component: ViewDoctorComponent},
  //   {path : 'patient/:id', component: ViewPatientComponent},
  // ], canActivate: [AuthguardGuard]},
  // {path : 'login', component : LoginComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
