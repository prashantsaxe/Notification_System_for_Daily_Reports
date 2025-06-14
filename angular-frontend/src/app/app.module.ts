import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NotebookRendererComponent } from './components/notebook-renderer/notebook-renderer.component';
import { ApiService } from './services/api.service';

@NgModule({
  declarations: [
    AppComponent,
    NotebookRendererComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [ApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }