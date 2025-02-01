import random

class Environment:
    def __init__(self):
        self.hospital_layout = {
            'Storage': 'Medicine Storage',
            'Room 101': {'patient_id': 1, 'medicine': 'Paracetamol', 'schedule': '08:00 AM'},
            'Room 102': {'patient_id': 2, 'medicine': 'Ibuprofen', 'schedule': '09:00 AM'},
            'Room 103': {'patient_id': 3, 'medicine': 'Antibiotic', 'schedule': '10:00 AM'},
            'Nurse Station': 'Nurse Assistance'
        }
        self.staff_available = True 

    def get_medicine_info(self, room):
        return self.hospital_layout.get(room, None)

    def check_staff_availability(self):
        return self.staff_available

    def show_status(self):
        print("\n🏥 Hospital Layout:")
        for location, details in self.hospital_layout.items():
            print(f"📍 {location}: {details}")

class Robot:
    def __init__(self):
        self.position = 'Storage'  
        self.medicine = None

    def move(self, destination):
        print(f"🤖 Moving to {destination}...")
        self.position = destination

    def pick_up_medicine(self, medicine):
        print(f"📦 Picking up {medicine} from storage...")
        self.medicine = medicine

    def scan_patient_id(self, patient_id):
        scanned_id = random.randint(1, 3) 
        print(f"📡 Scanning patient ID... Detected ID: {scanned_id}")
        return scanned_id == patient_id 

    def deliver_medicine(self, room, environment):
        patient_info = environment.get_medicine_info(room)
        if not patient_info:
            print(f"❌ Room {room} not found.")
            return

        if self.medicine != patient_info['medicine']:
            print(f"⚠️ Incorrect medicine! Expected: {patient_info['medicine']}, Found: {self.medicine}")
            return

        print(f"📄 Verifying patient ID in {room}...")
        if self.scan_patient_id(patient_info['patient_id']):
            print(f"✅ Medicine {self.medicine} successfully delivered to {room} at {patient_info['schedule']}!")
            self.medicine = None
        else:
            print("🚨 Patient ID mismatch! Alerting nurses...")
            if environment.check_staff_availability():
                print("👨‍⚕️ Nurse assistance requested.")
            else:
                print("❗ No nurse available. Emergency alert sent.")

    def run(self, environment):
        environment.show_status()
        
        for room in ['Room 101', 'Room 102', 'Room 103']:
            patient_info = environment.get_medicine_info(room)
            if not patient_info:
                continue
            
            self.move('Storage')
            self.pick_up_medicine(patient_info['medicine'])

            self.move(room)
            self.deliver_medicine(room, environment)

        print("\n✅ All medicine deliveries completed!")

environment = Environment()
robot = Robot()
robot.run(environment)

