#include<Servo.h>

/*
  _                               
 | |                              
 | |__  _   _  ___ __ _ _ __ ___  
 | '_ \| | | |/ __/ _` | '_ ` _ \ 
 | | | | |_| | (_| (_| | | | | | |
 |_| |_|\__, |\___\__,_|_| |_| |_|
         __/ |                    
        |___/                     

A Smart camera for hybrid teaching.
Muhamad Rifaldi | 05311840000022

github.com/retruxstudio/hycam

*/

Servo x, y, x2;
int s = 15;
int d = 30;
int xback, yback;

// Value ukuran camera stream
// int width = 640, height = 480;

// Custom ukuran camera stream
int width = 1280, height = 720;

// Posisi awal kedua servo
int xpos = 90, ypos = 90, x2pos = 180;

// Parameter value dari python
int x_mid, y_mid, c;

void setup() {

  Serial.begin(115200);
  
  x.attach(13);
  y.attach(12);
  x2.attach(14);

  x2.write(x2pos);
  x.write(xpos);
  y.write(ypos);
}

// Value penambahan dan pengurangan sudut
const int angle = 2;

void loop() { 

  if (Serial.available() > 0)
  {    

    // Baca dan simpan value center x-coordinate
    if (Serial.read() == 'X')
    {
      x_mid = Serial.parseInt();
      
      // Baca dan simpan value center y-coordinate
      if (Serial.read() == 'Y')
        y_mid = Serial.parseInt();
        
        // Baca dan simpan value C
        if (Serial.read() == 'C')
          c = Serial.parseInt();
      
    }

    // Angle kembali ke 90 ketika program ditutup
    if (c == 1) {
      xslow(90);
      yslow(90);
      x2slow(180); 
    } else if (c == 2) {

      xback = xpos;
      yback = ypos;      
      
      yslow(90);
      xslow(90);
      x2slow(0);

      // Fungsi servo control 
      // pos();
    
    } else if (c == 3) {
      
      x2slow(180);
      xslow(xback);
      yslow(yback);


      // pos();

    } else if (c == 4) {

      xback = xpos;
      yback = ypos;
      
      yslow(120);
      x2slow2(0);
      xslow2(0);
      xslow2(xback);
      x2slow2(180);
      yslow(ypos);

      // pos();

    } else {

      pos();

    }

  }
}

void pos() {

    // Control servo agar mengikuti gerak koordinat wajah
    if (x_mid > width / 2 + 75)
      xpos += angle;
    if (x_mid < width / 2 - 75)
      xpos -= angle;
    if (y_mid < height / 2 + 75)
      ypos -= angle;
    if (y_mid > height / 2 - 75)
      ypos += angle;

    // Keep agar sudut servo tetap di take area
    if (xpos >= 180)
      xpos = 180;
    else if (xpos <= 0)
      xpos = 0;
    if (ypos >= 180)
      ypos = 180;
    else if (ypos <= 0)
      ypos = 0;

    x.write(xpos);
    y.write(ypos);

}

void xslow (int i) { 
    
    xpos =x.read(); 
                     
    if ( i >= xpos) {
        for (xpos = xpos; xpos <= i; xpos=xpos +1) {
            x.write(xpos);                             
            delay(s); 
        }
    } else {
        for (xpos = xpos; xpos >= i; xpos=xpos- 1) {
            x.write(xpos);
            delay(s); 
        } 
    }
                      
}

void yslow (int i) { 
    
    ypos =y.read(); 
                     
    if ( i >= ypos) {
        for (ypos = ypos; ypos <= i; ypos=ypos +1) {
            y.write(ypos);                             
            delay(s); 
        }
    } else {
        for (ypos = ypos; ypos >= i; ypos=ypos- 1) {
            y.write(ypos);
            delay(s); 
        } 
    }
                      
}

void xslow2 (int i) { 
    
    xpos =x.read(); 
                     
    if ( i >= xpos) {
        for (xpos = xpos; xpos <= i; xpos=xpos +1) {
            x.write(xpos);                             
            delay(d); 
        }
    } else {
        for (xpos = xpos; xpos >= i; xpos=xpos- 1) {
            x.write(xpos);
            delay(d); 
        } 
    }
                      
}

void x2slow (int i) { 
    
    x2pos =x2.read(); 
                     
    if ( i >= x2pos) {
        for (x2pos = x2pos; x2pos <= i; x2pos=x2pos +1) {
            x2.write(x2pos);                             
            delay(s); 
        }
    } else {
        for (x2pos = x2pos; x2pos >= i; x2pos=x2pos- 1) {
            x2.write(x2pos);
            delay(s); 
        } 
    }
                      
}

void x2slow2 (int i) { 
    
    x2pos =x2.read(); 
                     
    if ( i >= x2pos) {
        for (x2pos = x2pos; x2pos <= i; x2pos=x2pos +1) {
            x2.write(x2pos);                             
            delay(d); 
        }
    } else {
        for (x2pos = x2pos; x2pos >= i; x2pos=x2pos- 1) {
            x2.write(x2pos);
            delay(d); 
        } 
    }
                      
}