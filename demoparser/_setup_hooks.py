from distutils.spawn import find_executable
from setuptools.command.build_py import build_py as _build_py
import glob
import subprocess


class ProtobufBuilder(_build_py):
    command_name = 'build_py'

    def protoc(self):
        proto_files = glob.glob('demoparser/protobufs/*.proto')
        subprocess.run([
            'protoc',
            '--python_out=.',
            #'--proto_path=demoparser/protobufs/',
            '--proto_path=.',
            *proto_files
        ], check=True)

    def run(self):
        self.protoc()
        _build_py.run(self)
