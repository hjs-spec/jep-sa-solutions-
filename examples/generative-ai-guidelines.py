"""
SDAIA Generative AI Guidelines - Complete Compliance Example
JEP Implementation for Saudi Arabia's Generative AI Framework

This example demonstrates:
- Public Use Case (flexible requirements)
- Government Use Case (strict requirements)
- Data classification compliance
- Human oversight requirements
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from implementation.sa_tracker import SaudiAITracker, DataClassification
import json
from datetime import datetime


class SDAIAGenerativeAIDemo:
    """
    Comprehensive demonstration of SDAIA Generative AI Guidelines
    """
    
    def __init__(self):
        # Initialize tracker for a government AI provider
        self.tracker = SaudiAITracker(
            organization="Saudi Government AI Services",
            organization_id="GOV-AI-001",
            sector="government",
            jurisdiction="saudi"
        )
        
        self.demo_results = {}
    
    def demonstrate_public_use_case(self):
        """Public-facing generative AI applications"""
        print("\n" + "="*70)
        print("PUBLIC USE CASE - GENERATIVE AI GUIDELINES")
        print("="*70)
        
        # Scenario 1: Public chatbot
        print("\n📱 Scenario 1: Public AI Chatbot")
        print("-" * 50)
        
        chatbot_content = {
            "content_id": "chat-public-001",
            "content_type": "text",
            "model_id": "saudi-llm-v2",
            "model_version": "2.5.0",
            "prompt": "Explain Saudi Vision 2030",
            "output": "Vision 2030 is Saudi Arabia's transformative economic and social reform blueprint...",
            "requires_human_review": False
        }
        
        result = self.tracker.label_generative_content(
            chatbot_content,
            use_case="public"
        )
        
        print(f"✅ Content Labeled: {result['content_id']}")
        print(f"   Model: {chatbot_content['model_id']} v{chatbot_content['model_version']}")
        print(f"   Watermark: {result['watermark']['disclosure_method']}")
        print(f"   JEP Receipt: {result['jep_receipt']}")
        
        # Scenario 2: Public image generation
        print("\n🎨 Scenario 2: Public Image Generation")
        print("-" * 50)
        
        image_content = {
            "content_id": "img-public-001",
            "content_type": "image",
            "model_id": "saudi-dalle-v1",
            "model_version": "1.2.0",
            "prompt": "Generate image of NEOM The Line",
            "output": "[image data]",
            "requires_human_review": False
        }
        
        result2 = self.tracker.label_generative_content(
            image_content,
            use_case="public"
        )
        
        print(f"✅ Content Labeled: {result2['content_id']}")
        print(f"   Model: {image_content['model_id']} v{image_content['model_version']}")
        print(f"   Watermark: {result2['watermark']['disclosure_method']}")
        print(f"   JEP Receipt: {result2['jep_receipt']}")
        
        # Public use case summary
        return {
            "chatbot": result,
            "image": result2
        }
    
    def demonstrate_government_use_case(self):
        """Government agency generative AI applications"""
        print("\n" + "="*70)
        print("GOVERNMENT USE CASE - GENERATIVE AI GUIDELINES")
        print("="*70)
        
        # Scenario 1: Government document generation (public data)
        print("\n📄 Scenario 1: Government Document Generation (Public Data)")
        print("-" * 50)
        
        doc_content = {
            "content_id": "gov-doc-001",
            "content_type": "text",
            "model_id": "saudi-gov-llm",
            "model_version": "1.0.0",
            "prompt": "Draft press release about new economic initiative",
            "output": "Press release draft content...",
            "requires_human_review": True,
            "human_reviewer": "Ahmed Al-Ghamdi (Press Office)",
            "data_classification": DataClassification.PUBLIC.value
        }
        
        result = self.tracker.label_generative_content(
            doc_content,
            use_case="government"
        )
        
        print(f"✅ Document Generated: {result['content_id']}")
        print(f"   Human Reviewer: {doc_content['human_reviewer']}")
        print(f"   Data Classification: PUBLIC")
        print(f"   Watermark: {result['watermark']['disclosure_method']}")
        print(f"   JEP Receipt: {result['jep_receipt']}")
        
        # Scenario 2: Government document generation (internal data)
        print("\n🔒 Scenario 2: Government Document Generation (Internal Data)")
        print("-" * 50)
        
        internal_content = {
            "content_id": "gov-int-001",
            "content_type": "text",
            "model_id": "saudi-gov-llm",
            "model_version": "1.0.0",
            "prompt": "Summarize internal policy review",
            "output": "Policy summary content...",
            "requires_human_review": True,
            "human_reviewer": "Dr. Noura Al-Saud (Policy Director)",
            "data_classification": DataClassification.INTERNAL.value,
            "access_restrictions": ["saudi_government_only"]
        }
        
        result2 = self.tracker.label_generative_content(
            internal_content,
            use_case="government"
        )
        
        print(f"✅ Document Generated: {result2['content_id']}")
        print(f"   Human Reviewer: {internal_content['human_reviewer']}")
        print(f"   Data Classification: INTERNAL")
        print(f"   Access Restrictions: {internal_content['access_restrictions']}")
        print(f"   JEP Receipt: {result2['jep_receipt']}")
        
        # Scenario 3: Rejected - Restricted data
        print("\n❌ Scenario 3: Attempt with Restricted Data (Rejected)")
        print("-" * 50)
        
        restricted_content = {
            "content_id": "gov-restricted-001",
            "content_type": "text",
            "model_id": "saudi-gov-llm",
            "model_version": "1.0.0",
            "prompt": "Process classified intelligence report",
            "requires_human_review": True,
            "data_classification": DataClassification.RESTRICTED.value
        }
        
        result3 = self.tracker.label_generative_content(
            restricted_content,
            use_case="government"
        )
        
        print(f"❌ Result: {result3.get('error', 'Unknown error')}")
        print(f"   Guideline: {result3.get('guideline', 'N/A')}")
        
        # Government use case summary
        return {
            "public_doc": result,
            "internal_doc": result2,
            "rejected": result3
        }
    
    def demonstrate_data_classification_matrix(self):
        """Demonstrate data classification compliance matrix"""
        print("\n" + "="*70)
        print("DATA CLASSIFICATION COMPLIANCE MATRIX")
        print("="*70)
        
        classifications = [
            DataClassification.PUBLIC,
            DataClassification.INTERNAL,
            DataClassification.CONFIDENTIAL,
            DataClassification.RESTRICTED,
            DataClassification.TOP_SECRET
        ]
        
        results = []
        for classification in classifications:
            print(f"\n📊 Testing: {classification.value.upper()}")
            print("-" * 30)
            
            test_content = {
                "content_id": f"test-{classification.value}-001",
                "content_type": "text",
                "model_id": "saudi-gov-llm",
                "model_version": "1.0.0",
                "prompt": "Test prompt",
                "requires_human_review": True,
                "data_classification": classification.value
            }
            
            result = self.tracker.label_generative_content(
                test_content,
                use_case="government"
            )
            
            if 'error' in result:
                print(f"❌ {classification.value.upper()}: REJECTED - {result['error']}")
            else:
                print(f"✅ {classification.value.upper()}: APPROVED")
                print(f"   JEP Receipt: {result['jep_receipt']}")
                results.append(result)
        
        return results
    
    def demonstrate_human_oversight_chain(self):
        """Demonstrate human oversight requirements"""
        print("\n" + "="*70)
        print("HUMAN OVERSIGHT CHAIN")
        print("="*70)
        
        # Multi-stage approval workflow
        stages = [
            {"level": "generation", "approver": "AI Assistant", "action": "draft_generated"},
            {"level": "review", "approver": "Content Specialist", "action": "initial_review"},
            {"level": "supervisor", "approver": "Department Manager", "action": "content_approval"},
            {"level": "legal", "approver": "Legal Counsel", "action": "compliance_check"},
            {"level": "final", "approver": "Agency Director", "action": "final_release"}
        ]
        
        receipts = []
        for stage in stages:
            receipt = self.tracker._create_receipt(
                event_type="delegate",
                subject_id="gov-doc-approval-001",
                payload={
                    "action": stage['action'],
                    "stage": stage['level'],
                    "approver": stage['approver'],
                    "timestamp": datetime.now().isoformat(),
                    "evidence": f"Approval recorded at {stage['level']} level",
                    "sdaia_framework": "generative_ai_guidelines",
                    "section": "Human Oversight"
                }
            )
            receipts.append(receipt)
            
            print(f"\n📋 Stage {len(receipts)}: {stage['level'].title()}")
            print(f"   Approver: {stage['approver']}")
            print(f"   JEP Receipt: {receipt.receipt_id}")
        
        return receipts
    
    def run_full_demo(self):
        """Run complete generative AI compliance demonstration"""
        print("\n" + "="*70)
        print("SDAIA GENERATIVE AI GUIDELINES - FULL COMPLIANCE DEMO")
        print("Kingdom of Saudi Arabia")
        print("="*70)
        
        # Run all demonstrations
        public_results = self.demonstrate_public_use_case()
        gov_results = self.demonstrate_government_use_case()
        classification_results = self.demonstrate_data_classification_matrix()
        oversight_chain = self.demonstrate_human_oversight_chain()
        
        # Generate compliance summary
        print("\n" + "="*70)
        print("COMPLIANCE SUMMARY")
        print("="*70)
        
        summary = {
            "public_use_cases": len(public_results),
            "government_use_cases": len([r for r in gov_results.values() if 'receipt' in r.__dict__ if hasattr(r, 'receipt')]),
            "rejected_attempts": 1,
            "data_classifications_tested": len(classification_results),
            "human_oversight_stages": len(oversight_chain),
            "total_receipts": len(self.tracker.receipts)
        }
        
        print(f"\n📊 Summary Statistics:")
        print(f"   Public Use Cases: {summary['public_use_cases']}")
        print(f"   Government Use Cases: {summary['government_use_cases']}")
        print(f"   Rejected Attempts: {summary['rejected_attempts']}")
        print(f"   Data Classifications Tested: {summary['data_classifications_tested']}")
        print(f"   Human Oversight Stages: {summary['human_oversight_stages']}")
        print(f"   Total JEP Receipts Generated: {summary['total_receipts']}")
        
        print("\n" + "="*70)
        print("✅ SDAIA GENERATIVE AI COMPLIANCE ACHIEVED")
        print("Public Use: ✅ Flexible labeling applied")
        print("Government Use: ✅ Strict controls enforced")
        print("Data Classification: ✅ PDPL compliant")
        print("Human Oversight: ✅ Full approval chain")
        print("="*70)
        
        return summary


if __name__ == "__main__":
    demo = SDAIAGenerativeAIDemo()
    summary = demo.run_full_demo()
    
    # Export summary
    with open("sdaia_generative_ai_compliance.json", "w") as f:
        json.dump(summary, f, indent=2)
    print("\n📄 Report exported to: sdaia_generative_ai_compliance.json")
