
import subprocess
import json


class MobileDevice(object):
	def __init__(self, serial_number):
		self.serial = serial_number
		self.sdk = self.get_device_parameter('sdk')
		self.os = self.get_device_parameter('os_version')
		self.manufacturer = self.get_device_parameter('manufacturer')
		self.gms_version = self.get_device_parameter('gms')
		self.bootloader_lock_status = self.get_device_parameter('bootloader_unlocked')


	def reboot_device(self):
		""" 
		Function that reboots the MobileDevice object
		"""
		reboot_command = 'adb reboot -s %r' % self.serial
		print "Rebooting %s" % self.serial
		try:
			subprocess.Popen(reboot_command, shell=True, executable='/bin/bash')
		except subprocess.CalledProcessError as error_message:
				print error_message.output


	def get_device_parameter(self, target_device_parameter):
		"""
		Function that queries the MobileDevice object for provided parameter if it exist in the dictionary 
		"""
		# Note:  At some point this needs to be moved out 
		available_device_parameters = {'sdk':'ro.build.version.sdk', 'serial':'ro.boot.serialno', 
		'bootloader_unlocked':'sys.oem_unlock_allowed', 'manufacturer':'ro.product.manufacturer',
		'model':'ro.product.model', 'gms':'ro.com.google.gmsversion', 'os_version':'ro.build.version.release'}

		if target_device_parameter in available_device_parameters:
			property_command = 'adb -s %r shell getprop %s' % (self.serial, available_device_parameters[target_parameter])
			try:
				return subprocess.check_output(property_command, shell=True, executable='/bin/bash')	
			except subprocess.CalledProcessError as error_message:
				print error_message.output
		else:
			return 'Err: parameter not available'


	def get_installed_apps(self, app_type):
		target_package_type = app_type
		if target_package_type == 'all':
			app_list_type = ''
		elif target_package_type == 'system':
			app_list_type = '-s'
		elif target_package_type == 'thirdparty':
			app_list_type = '-3'
		else:
			return	

		packages_command = 'adb -s %r shell pm list packages %s' % (self.serial, app_list_type)
		try:
			# return subprocess.check_output(packages_command, shell=True, executable='/bin/bash')	
			available_packages = subprocess.check_output(packages_command, shell=True, executable='/bin/bash')	
			return available_packages.split('\r\n')
		except subprocess.CalledProcessError as error_message:
			print error_message.output


	def load_snapshot(self):
		pass


	def create_app_delete_list(self):
		pass

















