#!/usr/bin/python
import pygtk
pygtk.require('2.0')
import gtk
import serial

class Agilent6612C:
    def __init__(self, port, baudrate):
        self.serial = serial.Serial(port, baudrate, rtscts=0, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

        self.serial.write("*cls\r\n")

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        main_box = gtk.VBox(False, 10)
        self.window.add(main_box)

        instrument_box = gtk.HBox(False, 10)
        main_box.pack_start(instrument_box)
        frame = gtk.Frame("Instrument")
        instrument_id = self.read_id()
        
        frame.add(gtk.Label(instrument_id))
        instrument_box.pack_start(frame)

        frame = gtk.Frame("Version")
        frame.add(gtk.Label(self.read_version()))
        instrument_box.pack_start(frame)
    
        box1 = gtk.HBox(False, 5)
        main_box.pack_start(box1)
        
        box5 = gtk.HBox(False, 5)
        main_box.pack_start(box5)

        box2 = gtk.HBox(False, 5)
        main_box.pack_start(box2)
        
        box3 = gtk.HBox(False, 5)
        main_box.pack_start(box3)
        
        box4 = gtk.HBox(False, 5)
        main_box.pack_start(box4)
        
        bottom_spacer_box = gtk.HBox(False, 10)
        main_box.pack_start(bottom_spacer_box)

        self.set_voltage = gtk.Label()
        frame = gtk.Frame("Set Voltage")
        frame.add(self.set_voltage)
        box1.pack_start(frame, False, False, 10)

        self.set_current = gtk.Label()
        frame = gtk.Frame("Set Current")
        frame.add(self.set_current)
        box1.pack_start(frame, False, False, 10)

        self.output = gtk.Label()
        frame = gtk.Frame("Output")
        frame.add(self.output)
        box1.pack_start(frame, False, False, 10)



#-----------------------
# Battery charging safties
#-----------------------
#       self.ovp = gtk.Entry()
#       self.ovp.set_max_length(6)
#       
#       
#       self.ovp_val = "6.00"
#       self.cutoff_curr_val = "0.030"
#       
#       self.ovp.connect("activate", self.enter_callback, self.ovp)
#       
#       frame = gtk.Frame("Over Voltage Prot")        
#       frame.add(self.ovp)
#       box1.pack_start(frame, False, False, 5)
#       
#       self.cutoff_curr = gtk.Entry()
#       frame = gtk.Frame("Cutoff Current")
#       frame.add(self.cutoff_curr)
#       box1.pack_start(frame, False, False, 5)
#       
#       self.ovp.set_text(self.ovp_val)
#       self.cutoff_curr.set_text(self.cutoff_curr_val)
#       self.ovp = float(self.ovp_val)
#       self.cutoff_curr = float(self.cutoff_curr_val)

#-----------------------


#-----------------------
# Overvoltage safty
#-----------------------
        ovp = gtk.Entry()
        ovp.set_max_length(6)
        ovp_val = "4.210"
        ovp.connect("activate", self.ovp_callback)
        frame = gtk.Frame("Over Voltage Prot")        
        frame.add(ovp)
        box1.pack_start(frame, False, False, 5)
        ovp.set_text(ovp_val)
        ovp = float(ovp_val)
        
        myvolt = float(self.read_voltage())
        self.ovp = float(ovp_val)
        #if myvolt > self.ovp:
            #self.serial.write("outp 0\r\n")
#-----------------------


#-----------------------
# Current cutoff safety
#-----------------------
        cutoff_curr = gtk.Entry()
        cutoff_curr.set_max_length(6)
        cutoff_curr_val = "0.160"
        cutoff_curr.connect("activate", self.cutoff_curr_callback)
        frame = gtk.Frame("Cutoff Current")
        frame.add(cutoff_curr)
        box1.pack_start(frame, False, False, 5)
        
        cutoff_curr.set_text(cutoff_curr_val)
        #cutoff_curr = float(cutoff_curr_val)
        #mycurr = float(self.read_current())
        
        #if mycurr < cutoff_curr:
            #self.serial.write("outp 0\r\n")
#-----------------------


#-----------------------
# Main disply
#-----------------------    
        self.voltage = gtk.Label()
        frame = gtk.Frame("Measured Voltage")
        frame.add(self.voltage)
        box2.pack_start(frame, False, False, 10)

        self.current = gtk.Label()
        frame = gtk.Frame("Measured Current")
        frame.add(self.current)
        box2.pack_start(frame, False, False, 10)
        
        self.power = gtk.Label()
        frame = gtk.Frame("Calculated Power")
        frame.add(self.power)
        box2.pack_start(frame, False, False, 10)
         
        button1 = gtk.Button("  Local  ")
        button2 = gtk.Button(" Address ")
        button3 = gtk.Button("  Meter  ")
        button4 = gtk.Button("   Up    ")
        button5 = gtk.Button(" Voltage ")
        button6 = gtk.Button(" Output  ")
        button7 = gtk.Button("Enter Num")
        button11 = gtk.Button("  Blue   ")
        button12 = gtk.Button(" Recall  ")
        button13 = gtk.Button(" Protect ")
        button14 = gtk.Button("  Down   ")
        button15 = gtk.Button(" Current ")
        button16 = gtk.ToggleButton(" On/Off  ")
        button17 = gtk.Button(" Enter   ")
            
        button1.set_size_request(90, 25)
        button2.set_size_request(90, 25)
        button3.set_size_request(90, 25)
        button4.set_size_request(90, 25)
        button5.set_size_request(90, 25)
        button6.set_size_request(90, 25)
        button7.set_size_request(90, 25)
        button11.set_size_request(90, 25)
        button12.set_size_request(90, 25)
        button13.set_size_request(90, 25)
        button14.set_size_request(90, 25)
        button15.set_size_request(90, 25)
        button16.set_size_request(90, 25)
        button17.set_size_request(90, 25)

        button1.set_sensitive(False)
        button2.set_sensitive(False)
        button3.set_sensitive(False)
        button4.set_sensitive(False)
        button5.set_sensitive(False)
        button6.set_sensitive(False)
        button7.set_sensitive(False)
        button11.set_sensitive(False)
        button12.set_sensitive(False)
        button13.set_sensitive(False)
        button14.set_sensitive(False)
        button15.set_sensitive(False)
        button16.set_sensitive(True)
        button17.set_sensitive(False)

        box3.pack_start(button1, False, False, 12)
        box3.pack_start(button2, False, False, 12)
        box3.pack_start(button3, False, False, 12)
        box3.pack_start(button4, False, False, 12)
        box3.pack_start(button5, False, False, 12)
        box3.pack_start(button6, False, False, 12)
        box3.pack_start(button7, False, False, 12)
        box4.pack_start(button11, False, False, 12)
        box4.pack_start(button12, False, False, 12)
        box4.pack_start(button13, False, False, 12)
        box4.pack_start(button14, False, False, 12)
        box4.pack_start(button15, False, False, 12)
        box4.pack_start(button16, False, False, 12)
        box4.pack_start(button17, False, False, 12)
 
        button16.connect("clicked", self.enable_output)
        
        recall0_button = gtk.Button(" Recall 0 ")
        recall1_button = gtk.Button(" Recall 1 ")
        recall2_button = gtk.Button(" Recall 2 ")
        recall3_button = gtk.Button(" Recall 3 ")
        save0_button = gtk.Button(" Save 0  ")
        save1_button = gtk.Button(" Save 1  ")
        save2_button = gtk.Button(" Save 2  ")
        save3_button = gtk.Button(" Save 3  ")
        
        recall0_button.set_size_request(90, 25)
        recall1_button.set_size_request(90, 25)
        recall2_button.set_size_request(90, 25)
        recall3_button.set_size_request(90, 25)        
        save0_button.set_size_request(90, 25)
        save1_button.set_size_request(90, 25)
        save2_button.set_size_request(90, 25)
        save3_button.set_size_request(90, 25)        
        
        box5.pack_start(recall0_button, False, False, 4)
        box5.pack_start(recall1_button, False, False, 4)
        box5.pack_start(recall2_button, False, False, 4)
        box5.pack_start(recall3_button, False, False, 4)
        box5.pack_start(save0_button, False, False, 4)
        box5.pack_start(save1_button, False, False, 4)
        box5.pack_start(save2_button, False, False, 4)
        box5.pack_start(save3_button, False, False, 4)
        
        recall0_button.connect("clicked", self.recall_prog0)
        recall1_button.connect("clicked", self.recall_prog1)
        recall2_button.connect("clicked", self.recall_prog2)   
        recall3_button.connect("clicked", self.recall_prog3)
        save0_button.connect("clicked", self.save_prog0)
        save1_button.connect("clicked", self.save_prog1)
        save2_button.connect("clicked", self.save_prog2)   
        save3_button.connect("clicked", self.save_prog3)
 
        gtk.timeout_add(500, self.update)
        
        
        
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        #self.window.set_title((instrument_id.split(','))[0] + ' ' + (instrument_id.split(','))[1])
        self.window.set_title("Agilent 6612C - 40 Watt Programmable DC Power Supply")
        self.window.show_all()
#-----------------------       
        
        
        
        
        

    def delete_event(self, widget, event, data=None):
        return False

    def destroy(self, widget, data=None):
        self.serial.close()
        gtk.main_quit()

#-----------------------
# Update the measured values and recalculate power based on the new readings
#-----------------------
    def update(self):
        output = ' Off '
        if self.read_output() == 1:
            output = ' On '
            
        markup_span1 = '<span size="30000" color="white" bgcolor="green">'
        markup_span2 = '<span size="35000" color="white" bgcolor="blue">'
        self.set_voltage.set_markup(markup_span1 + self.read_set_voltage() +" V "+ '</span>')
        self.set_current.set_markup(markup_span1 + self.read_set_current() +" A "+ '</span>')
        self.output.set_markup(markup_span1 + output + '</span>')
        self.voltage.set_markup(markup_span2 + self.read_voltage() +" V " + '</span>')
        self.current.set_markup(markup_span2 + self.read_current() +" A "+ '</span>')
        self.power.set_markup(markup_span2 + self.calc_power() +" W " + '</span>')
        return True





    





    def read_id(self):
        self.serial.write("*idn?\r\n")
        return self.serial.readline().rstrip('\r\n')

    def read_version(self):
        self.serial.write("syst:vers?\r\n")
        return self.serial.readline().rstrip('\r\n')

    def read_set_voltage(self):
        self.serial.write("volt?\r\n")
        return '{:.6f}'.format(float(self.serial.readline()))

    def read_voltage(self):
        self.serial.write("meas:volt?\r\n")
        return '{:.6f}'.format(float(self.serial.readline()))
        
    def read_set_current(self):
        self.serial.write("curr?\r\n")
        return '{:.5f}'.format(float(self.serial.readline()))

    def read_current(self):
        self.serial.write("meas:curr?\r\n")
        return '{:.6f}'.format(float(self.serial.readline()))

    def read_output(self):
        self.serial.write("outp?\r\n")
        return int(self.serial.readline())

#-----------------------
# Power Calulation
#-----------------------        
    def calc_power(self):
        myvolt = float(self.read_voltage())
        mycurr = float(self.read_current())
        mypower = myvolt * mycurr        
        return '{:.6f}'.format(mypower)
#-----------------------


#-----------------------
# Overvoltage safty
#-----------------------
    def ovp_callback(self, widget):
        ovp_val = widget.get_text()
        myvolt = float(self.read_voltage())
        self.ovp = float(ovp_val)
        if myvolt > self.ovp:
            self.serial.write("outp 0\r\n")
#-----------------------





#-----------------------
# Current cutoff safety
#-----------------------

    def cutoff_curr_callback(self, widget):
        cutoff_curr_val = widget.get_text()
        mycurr = float(self.read_current())
        self.cutoff_curr = float(cutoff_curr_val)
        if mycurr < self.cutoff_curr:
            self.serial.write("outp 0\r\n")
            
#-----------------------            




            

    def enable_output(self, widget):
        if self.read_output() == 1:
            self.serial.write("outp 0\r\n")
        elif self.read_output() == 0:
            self.serial.write("outp 1\r\n")


#-----------------------
# Store and recall programs
#-----------------------            
    def recall_prog0(self, widget):
        self.serial.write("*rcl 0\r\n")
        
    def recall_prog1(self, widget):
        self.serial.write("*rcl 1\r\n")
        
    def recall_prog2(self, widget):
        self.serial.write("*rcl 2\r\n")                 
    
    def recall_prog3(self, widget):
        self.serial.write("*rcl 3\r\n")       
        
    def save_prog0(self, widget):
        self.serial.write("*sav 0\r\n")
        
    def save_prog1(self, widget):
        self.serial.write("*sav 1\r\n")
        
    def save_prog2(self, widget):
        self.serial.write("*sav 2\r\n")                 
    
    def save_prog3(self, widget):
        self.serial.write("*sav 3\r\n")
#-----------------------


    def main(self):
        gtk.main()

Baudrate = 9600
app = Agilent6612C("/dev/ttyUSB0", Baudrate)
app.main()
