#include "gb_common.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <dirent.h>
#include <fcntl.h>
#include <assert.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
void setup_gpio()
{
   // for this test we are only using GP18
   INP_GPIO(18);

   // enable pull-up on GPIO 18, set pull to 2 (code for pull high)
   GPIO_PULL = 2;
   short_wait();
   // setting bits 18 below means that the GPIO_PULL is applied to
   // GPIO 18
   GPIO_PULLCLK0 = 0x00040000;
   short_wait();
   GPIO_PULL = 0;
   GPIO_PULLCLK0 = 0;
} // setup_gpio

// remove pulling on pins so they can be used for somnething else next time
// gertboard is used
void unpull_pins()
{
   // disable pull-up on GPIO 18, set pull to 0 (code for no pull)
   GPIO_PULL = 0;
   short_wait();
   // setting bits 18 below means that the GPIO_PULL is applied to
   // GPIO 18
   GPIO_PULLCLK0 = 0x00040000;
   short_wait();
   GPIO_PULL = 0;
   GPIO_PULLCLK0 = 0;
} // unpull_pins

int main(void)
{
  unsigned int b;
  unsigned int flag=0;
  setup_io();
  // Set GPIO pin 18 to the required mode
  setup_gpio();

  while (1)
  {
    b = GPIO_IN0;
    b = (b >> 18 ) & 0x01; // keep only bit 18

    if (b==0) {
      flag=0;
      //printf("b is 0\n");
    }
    if (b==1) {
      flag++;
      if (flag==1) {
        system("sh /root/powersag.sh");
      }
      //printf("b is 1\n");
    }
    if (flag>=10) {
      system("sh /root/powerfail.sh");
      //printf("flag is 10+\nshutting down everything");
      break;
    }
    sleep(1);
  }
  unpull_pins();
  restore_io();
  return 0;
} // main

