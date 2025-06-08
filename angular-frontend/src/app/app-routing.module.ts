import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { NotebookRendererComponent } from './components/notebook-renderer/notebook-renderer.component';

const routes: Routes = [
  { path: '', redirectTo: '/notebooks', pathMatch: 'full' },
  { path: 'notebooks', component: NotebookRendererComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }