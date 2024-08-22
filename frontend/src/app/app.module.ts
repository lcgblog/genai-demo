import { provideHttpClient, withInterceptorsFromDi } from '@angular/common/http'; // Import provideHttpClient and withInterceptorsFromDi
import { NgModule } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatTableModule } from '@angular/material/table';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppComponent } from './app.component';
import { TableUpdatesComponent } from './components/table-updates/table-updates.component';

@NgModule({
  declarations: [
    AppComponent,
    TableUpdatesComponent
  ],
  imports: [
    BrowserModule,
    MatTableModule,
    MatButtonModule,
    BrowserAnimationsModule,
    
    // other imports
  ],
  providers: [
    provideHttpClient(withInterceptorsFromDi()) // Provide HttpClient with interceptors from DI
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }